from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
]
