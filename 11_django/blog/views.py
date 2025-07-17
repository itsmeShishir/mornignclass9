from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# inner working of template , views and urls 
# / -> request
# response -> response -> html, httpResponse, api -> json, redirect, xml, etc
#  2 types of Views -> FBV, CBV
# FBV -> function based views
#  def functionName(request):
#      return HttpResponse("<h1>hello this is home page</h1>")

def index(request):
    # return HttpResponse("<h1>hello this is home page</h1>")
    return render(request, "index.html")

def About(request):
    # return HttpResponse("<h1>hello this is About page</h1>")
    return render(request, "about.html")

def Category(request):
    # return HttpResponse("<h1>hello this is Category page</h1>")
    return render(request, "category.html")

def SingleCategory(request):
    return render(request, "singlecategory.html")
def Blog(request):
    return render(request, "blog.html")
def SingleBlog(request):
    return render(request, "post.html")
def Contact(request):
    return render(request, "contact.html")