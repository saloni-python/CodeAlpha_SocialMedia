from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("create-post/", views.create_post, name="create_post"),
    path("add-comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path("like/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path("follow/<int:user_id>/", views.toggle_follow, name="toggle_follow"),
    path("profile/<int:user_id>/", views.profile_view, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
]