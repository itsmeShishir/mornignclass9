from django.db import models
from django.utils.text import slugify
from customauthapp.models import CustomUser

# oop -> Class or Interface -> Model -> Sql -> ORM -> Database 
# ORM -> Object Relational Mapping
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = slugify(title)
    img = models.ImageField(upload_to="category/", null=True, blank=True)

    def __str__(self):
        return self.title 

class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = slugify(title)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    small_content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    home_page_show = models.BooleanField(default=False)
    featured_product = models.BooleanField(default=False)
    img = models.ImageField(upload_to="blog/", null=True, blank=True)
    content = models.TextField()
    price = models.IntegerField()
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.IntegerField(choices=rating)
    blog = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
    


