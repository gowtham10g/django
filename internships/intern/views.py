from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import InternshipRegisterForm

# Register View
def register(request):
    print("acessed login_view")
    if request.method == "POST":
        form = InternshipRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to the home page after registration
    else:
        form = InternshipRegisterForm()
    
    return render(request, "intern/register.html", {"form": form})


# Login View
def login_view(request):
    print("acessed login_view")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to home after login
    else:
        form = AuthenticationForm()

    return render(request, "intern/login.html", {"form": form})

# Home View (Authenticated User Only)
def home(request):
    print("acessed login_view")
    return render(request, 'intern/home.html')


def courses_view(request):
    return render(request, 'courses.html')

