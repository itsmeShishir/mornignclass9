from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from customauthapp.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator

# Create your views here.
# inner working of template , views and urls 
# / -> request
# response -> response -> html, httpResponse, api -> json, redirect, xml, etc
#  2 types of Views -> FBV, CBV
# FBV -> function based views
#  def functionName(request):
#      return HttpResponse("<h1>hello this is home page</h1>")

# 15 to 20 min 
# ORM -> data Show in UI
# 1. contact.save()
# 2. Contact.objects.create()
# 3. Blog.objects.all() -> select * from blog
# 4. Blog.objects.get(id=1) -> select * from blog where id = 1
# 5. Blog.objects.filter(featured_blog=True)
def index(request):
    blogs= Blog.objects.filter(home_page_show=True)
    category = Category.objects.all()
    feature_blog = Blog.objects.filter(featured_blog=True)
    feature_blogs = feature_blog.first()
    post = Blog.objects.all()
    context = {
        "blogs": blogs,
        "category": category,
        "feature_blogs": feature_blogs,
        "post": post
    }
    return render(request, "frontend/index.html", context)

def About(request):
    return render(request, "frontend/about.html")

def Categorys(request):
    return render(request, "frontend/category.html")

def SingleCategory(request, id):
    category = get_object_or_404(Category, id=id)
    blog = Blog.objects.filter(category=category)
    context = {
        "blog": blog
    }
    return render(request, "frontend/singlecategory.html", context)

def Blogs(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 12)
    pagination_number = request.GET.get("page")
    page_obj = paginator.get_page(pagination_number)
    category = Category.objects.all()
    context = {
        'page_obj': page_obj,
        'category': category
    }
    return render(request, "frontend/blog.html", context)

def SingleBlog(request, id):
    getSingle= get_object_or_404(Blog, id=id)
    context = {
        "getSingle": getSingle
    }
    return render(request, "frontend/post.html", context)

def Contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email= request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        # contact = Contact(name=name, email=email, subject=subject, message=message)
        # contact.save()
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Message Sent")
        return redirect("contactpage")
    return render(request, "frontend/contact.html")