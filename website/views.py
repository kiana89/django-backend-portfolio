from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def single_post(request):
    return render(request, 'single-post.html')