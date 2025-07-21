from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="homepage"),
    path("about", About, name="aboutpage"),
    path("category", Categorys, name="categorypage"),
    path("singlecategory", SingleCategory, name="Singlecategorypage"),
    path("blog", Blogs, name="blogpage"),
    path("singleblog/<int:id>", SingleBlog, name="singleblogpage"),
    path("contact", Contacts, name="contactpage"),
]