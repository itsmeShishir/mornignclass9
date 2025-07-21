from django.db import models
from django.utils.text import slugify
# oop -> Class or Interface -> Model -> Sql -> ORM -> Database 
# ORM -> Object Relational Mapping

# pip install Pillow
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    img = models.ImageField(upload_to="category/", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title 

class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    small_content = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    home_page_show = models.BooleanField(default=False)
    featured_blog = models.BooleanField(default=False)
    img = models.ImageField(upload_to="blog/", null=True, blank=True)
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.CharField(max_length=255)
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
    
# cmd -> activate
# (env) -> pip install Pillow
# (env) -> python manage.py makemigration
# (env) -> python manage.py migrate

