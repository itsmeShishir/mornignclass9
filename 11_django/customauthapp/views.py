from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def logouts(request):
    return render(request, "index.html")

