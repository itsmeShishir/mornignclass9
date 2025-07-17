from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="homepage"),
    path("about", About, name="aboutpage"),
    path("category", Category, name="categorypage"),
    path("singlecategory", SingleCategory, name="Singlecategorypage"),
    path("blog", Blog, name="blogpage"),
    path("singleblog", SingleBlog, name="singleblogpage"),
    path("contact", Contact, name="contactpage"),
]