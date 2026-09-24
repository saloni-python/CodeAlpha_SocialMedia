from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile, Post, Comment, Like, Follow


@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    users = User.objects.exclude(id=request.user.id)

    return render(
        request,
        "social/home.html",
        {
            "posts": posts,
            "users": users
        }
    )


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(user=user)

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "social/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "social/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST["content"]

        if content.strip():
            Post.objects.create(
                author=request.user,
                content=content
            )

        return redirect("home")


@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        content = request.POST["content"]

        if content.strip():
            post = Post.objects.get(id=post_id)

            Comment.objects.create(
                post=post,
                user=request.user,
                content=content
            )

    return redirect("home")


@login_required
def toggle_like(request, post_id):
    post = Post.objects.get(id=post_id)

    like = Like.objects.filter(
        post=post,
        user=request.user
    ).first()

    if like:
        like.delete()
    else:
        Like.objects.create(
            post=post,
            user=request.user
        )

    return redirect("home")


@login_required
def toggle_follow(request, user_id):
    target_user = User.objects.get(id=user_id)

    if target_user == request.user:
        return redirect("home")

    follow = Follow.objects.filter(
        follower=request.user,
        following=target_user
    ).first()

    if follow:
        follow.delete()
    else:
        Follow.objects.create(
            follower=request.user,
            following=target_user
        )

    return redirect("home")


@login_required
def profile_view(request, user_id):
    profile_user = User.objects.get(id=user_id)

    profile, created = Profile.objects.get_or_create(
        user=profile_user
    )

    posts = Post.objects.filter(
        author=profile_user
    ).order_by("-created_at")

    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    is_following = Follow.objects.filter(
        follower=request.user,
        following=profile_user
    ).exists()

    return render(
        request,
        "social/profile.html",
        {
            "profile_user": profile_user,
            "profile": profile,
            "posts": posts,
            "followers_count": followers_count,
            "following_count": following_count,
            "is_following": is_following,
        }
    )
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        request.user.email = request.POST["email"]
        request.user.save()

        profile.bio = request.POST["bio"]
        profile.save()

        return redirect("profile", user_id=request.user.id)

    return render(
        request,
        "social/edit_profile.html",
        {
            "profile": profile
        }
    )