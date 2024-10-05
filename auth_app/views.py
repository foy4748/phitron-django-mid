from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.urls import reverse_lazy

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

    return render(req, "auth_app/registration_form.html", {"form": form})


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

    return render(req, "auth_app/login_form.html", {"form": form})


def LogoutUser(req):
    logout(req)
    messages.success(req, "Logged Out")
    return redirect("/")


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("car:car_list")
    template_name = "auth_app/change_password.html"

    def form_valid(self, form):
        messages.success(self.request, "Changed password successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "FAILED to Change password")
        return super().form_invalid(form)
