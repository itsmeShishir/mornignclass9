from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Contact
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from blog.models import Blog, Comment, Category, Tag
from .forms import TagForm, CategoryForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
#  reverse_lazy 
from django.urls import reverse_lazy

# 2 types -> Custom User Form , Forms.py ->> bootstrap forms
# @login_required

from django.contrib.auth.decorators import login_required
def logins(request):
    if request.method == "POST":   
        email = request.POST.get("email")
        password = request.POST.get("password")
        user= authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            if user.role == "admin":
                messages.success(request, "Login Success")
                return redirect("admin_page")
            elif user.role == "user":
                messages.success(request, "Login Success")
                return redirect("profiles")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")
    return render(request, "login.html")

def register(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email= request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        phone_number = request.POST.get("phone_number")
        user_profile = request.POST.get("user_profile")
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")
        user = CustomUser.objects.create_user(email=email, password=password, name=name, phone_number=phone_number, user_profile=user_profile)
        user.save()
        messages.success(request, "Registration Success")
        return redirect("login")
    return render(request, "register.html")
            
@login_required
def logouts(request):
    logout(request)
    return redirect("login")

@login_required
def profiles(request):
    if request.user.role != "user":
        messages.error(request, "Access Denied")
        return redirect("admin_page")
    
    users = request.user
    context = {
        "users": users
    }
    return render(request, "profile.html", context)

@login_required
def update_profile(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email= request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        user_profile = request.POST.get("user_profile")
        user = request.user
        user.name = name
        user.email = email
        user.phone_number = phone_number
        user.user_profile = user_profile
        user.save()
        messages.success(request, "Profile Updated")
        return redirect("profiles")
    return render(request, "update_profile.html")

@login_required
def change_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("change_password")
        user = request.user
        user.set_password(password)
        user.save()
        messages.success(request, "Password Updated")
        return redirect("profiles")
    return render(request, "change_password.html")

@login_required
def admins_page(request):
    if request.user.role != "admin":
        messages.error(request, "Access Denied")
        return redirect("profiles")
    users = CustomUser.objects.all()
    usercount = users.count()
    blog = Blog.objects.all()
    comment = Comment.objects.all()
    category = Category.objects.all()
    contact = Contact.objects.all()
    context = {
        "users": users,
        "usercount": usercount,
        "blog": blog,
        "comment": comment,
        "category": category,
        "contact": contact
    }
    return render(request, "admins/admin.html", context)

@login_required
def add_new_blog(request):
    if request.user.role != "admin":
        messages.error(request, "Access Denied")
        return redirect("profiles")
    categories = Category.objects.all()
    tag = Tag.objects.all()
    context = {
        "categories": categories,
        "tag": tag
    }
    if request.method == "POST":
        title = request.POST.get("title")
        small_content = request.POST.get("small_content")
        content = request.POST.get("content")
        slug = request.POST.get("slug")
        home_page_show = request.POST.get("home_page_show") == "on"
        featured_blog = request.POST.get("featured_blog") == "on"
        img = request.FILES.get("img")
        category = Category.objects.get(id = request.POST.get("category"))
        tag_id = request.POST.getlist("tag")
        blog = Blog.objects.create(
            title=title, 
            small_content=small_content, 
            content=content, 
            slug=slug, 
            home_page_show=home_page_show, 
            featured_blog=featured_blog, 
            img=img, 
            category=category
        )
        blog.tag.set(tag_id)
        messages.success(request, "Blog Added")
        return redirect("admin_page")
    return render(request, "admins/add_new_blog.html", context)

@login_required
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.user.role != "admin":
        messages.error(request, "Access Denied")
        return redirect("profiles")
    categories = Category.objects.all()
    tag = Tag.objects.all()
    context = {
        "categories": categories,
        "tag": tag,
        "blog": blog
    }
    if request.method == "POST":
        blog.title = request.POST.get("title")
        blog.small_content = request.POST.get("small_content")
        blog.content = request.POST.get("content")
        blog.slug = request.POST.get("slug")
        blog.home_page_show = request.POST.get("home_page_show") == "on"
        blog.featured_blog = request.POST.get("featured_blog") == "on"
        if request.FILES.get("img"):
            blog.img = request.FILES.get("img")
        blog.category = Category.objects.get(id = request.POST.get("category"))
        tag_id = request.POST.getlist("tag")
        blog.save()
        blog.tag.set(tag_id)
        messages.success(request, "Blog Added")
        return redirect("admin_page")
    return render(request, "admins/add_new_blog.html", context)


@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.user.role != "admin":
        messages.error(request, "Access Denied")
        return redirect("profiles")
    blog.delete()
    messages.success(request, "Blog Deleted")
    return redirect("admin_page")

@login_required
def tag_admin_page(request):
    if request.user.role != "admin":
        messages.error(request, "Access Denied")
        return redirect("profiles")

    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag Added")
            return redirect("admin_page")
    else:
        form = TagForm()
    return render(request, "admins/tag.html", {"form": form})
# Category -> Crud using CBV
#list, create, update, delete, details
class CategoryList(ListView):
    model = Category
    template_name = "admins/category.html"
    context_object_name = "categories"

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "admins/createcategory.html"
    success_url = reverse_lazy("admin_page")

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "admins/updatecategory.html"
    success_url = reverse_lazy("admin_page")

class CategoryDelete(DeleteView):
    model = Category
    template_name = "admins/deletecategory.html"
    success_url = reverse_lazy("admin_page")