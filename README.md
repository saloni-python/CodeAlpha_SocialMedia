# CodeAlpha Social Media Platform

A simple Social Media Platform developed as part of the CodeAlpha Full Stack Development Internship.

## Features

- User Registration and Login
- User Profiles
- Edit Profile
- Create Posts
- View Recent Posts
- Like and Unlike Posts
- Add Comments
- Follow and Unfollow Users
- Followers and Following Count
- Django Admin Panel
- Responsive and Simple User Interface

## Technologies Used

- HTML
- CSS
- Python
- Django
- SQLite
- Git
- GitHub

## Project Structure

```text
CodeAlpha_SocialMedia/
│
├── manage.py
├── README.md
├── .gitignore
│
├── social/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── social/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── profile.html
│   │       └── edit_profile.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── socialmedia/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py