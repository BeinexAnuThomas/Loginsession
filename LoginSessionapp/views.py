from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import LoginForm
from .models import Login

# Create your views here.

def home(request):
    return render(request, "index.html")

def visit_count(request):
    page_count = int(request.COOKIES.get("page_count", 1))
    page_count += 1
    response = HttpResponse(f"Page visit count: {page_count}")
    response.set_cookie("page_count", page_count)
    return response

def clear_count(request):
    response = HttpResponse("Cookie cleared...")
    response.delete_cookie("page_count")
    return response

def login(request):    
    if 'email' in request.session:
        return redirect("profile")
    if request.method == "GET":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['email'] = form.cleaned_data['email']
            request.session['full_name'] = form.cleaned_data['full_name']
            request.session['gender'] = form.cleaned_data['gender']
            request.session['age'] = form.cleaned_data['age']
            return redirect("profile")
    return render(request, "login.html", {"form": form})

def profile(request):
    return render(request, "profile.html")

def logout(request):
    request.session.pop("email")
    request.session.pop("full_name")
    request.session.pop("gender")
    request.session.pop("age")
    return render(request, "logout.html")