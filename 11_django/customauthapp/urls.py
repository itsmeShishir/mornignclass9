from django.urls import path
from .views import *

urlpatterns = [
    path("login", logins, name="login"),
    path("register", register, name="register"),
    path("logout", logouts, name="logout"),
    path("profiles", profiles, name="profiles"),
    path("update_profile", update_profile, name="update_profile"),
    path("update_password", change_password, name="update_password"),
]