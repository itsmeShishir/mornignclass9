from django.urls import path
from .views import *

urlpatterns = [
    path("login", logins, name="login"),
    path("register", register, name="register"),
    path("logout", logouts, name="logout"),
    path("profiles", profiles, name="profiles"),
    path("update_profile", update_profile, name="update_profile"),
    path("update_password", change_password, name="update_password"),
    path("admin_page", admins_page, name="admin_page"),
    path("add_blog", add_new_blog, name="add_blog"),
    path("update_blog/<int:id>", update_blog, name="update_blog"),
    path("delete_blog/<int:id>", delete_blog, name="delete_blog"),
]