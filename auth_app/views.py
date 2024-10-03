from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import messages

from auth_app.forms import RegisterForm


# Create your views here.
def ShowRegistrationForm(req):
    form = RegisterForm()
    if req.POST:
        print("Creating User")
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            print("User Created")
            uname = req.POST.get("username")
            pword = form.cleaned_data["password1"]
            print(uname, pword)
            current_user = authenticate(username=uname, password=pword)
            if current_user is not None:
                print("Logged in successfully")
                login(req, current_user)
                messages.success(req, "Logged in successfully")
                next_url = req.GET.get("next", "/")
                return redirect(next_url)
            else:
                print("FAILED to Login")
                messages.error(req, "FAILED to Login")
                return redirect("/")

    return render(req, "auth/registration_form.html", {"form": form})


def ShowLoginForm(req):
    form = AuthenticationForm()
    if req.POST:
        print("Logining in User")
        form = AuthenticationForm(req.POST)
        uname = req.POST.get("username")
        pword = req.POST.get("password")
        print(uname, pword)
        current_user = authenticate(username=uname, password=pword)
        if current_user is not None:
            print("Logged in successfully")
            login(req, current_user)
            messages.success(req, "Logged in successfully")
            next_url = req.GET.get("next", "/")
            return redirect(next_url)
        else:
            print("FAILED to Login")
            messages.error(req, "FAILED to Login")
            return redirect("/")

    return render(req, "auth/login_form.html", {"form": form})


def LogoutUser(req):
    logout(req)
    messages.success(req, "Logged Out")
    return redirect("/")
