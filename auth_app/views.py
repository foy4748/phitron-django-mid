from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from auth_app.forms import ChangeProfileForm, RegisterForm


# Create your views here.
class ShowRegistrationForm(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "auth_app/registration_form.html"

    def get_success_url(self):
        next_url = self.request.GET.get("next", reverse_lazy("car:car_list"))
        return next_url

    def form_valid(self, form):
        valid = super(ShowRegistrationForm, self).form_valid(form)
        username, password = form.cleaned_data.get("username"), form.cleaned_data.get(
            "password1"
        )
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        messages.success(self.request, "Registered and Logged in successfully")
        return valid


class ShowLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = "auth_app/login_form.html"

    def get_success_url(self):
        next_url = self.request.GET.get("next", reverse_lazy("car:car_list"))
        return next_url

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "FAILED to Login")
        return super().form_invalid(form)


def LogoutUser(req):
    logout(req)
    messages.success(req, "Logged Out")
    return redirect("/")


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("order_car:my_orders")
    template_name = "auth_app/change_password.html"

    def form_valid(self, form):
        messages.success(self.request, "Changed password successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "FAILED to Change password")
        return super().form_invalid(form)


class ChangeProfileView(UpdateView):
    form_class = ChangeProfileForm
    success_url = reverse_lazy("car:car_list")
    template_name = "auth_app/change_profile.html"

    def get_object(self, queryset=None):
        # This method is used to get the instance of the object to be updated
        return self.request.user


# Functional Views

# def ShowRegistrationForm(req):
#     form = RegisterForm()
#     if req.POST:
#         print("Creating User")
#         form = RegisterForm(req.POST)
#         if form.is_valid():
#             form.save()
#             print("User Created")
#             uname = req.POST.get("username")
#             pword = form.cleaned_data["password1"]
#             print(uname, pword)
#             current_user = authenticate(username=uname, password=pword)
#             if current_user is not None:
#                 print("Logged in successfully")
#                 login(req, current_user)
#                 messages.success(req, "Logged in successfully")
#                 next_url = req.GET.get("next", "/")
#                 return redirect(next_url)
#             else:
#                 print("FAILED to Login")
#                 messages.error(req, "FAILED to Login")
#                 return redirect("/")

#     return render(req, "auth_app/registration_form.html", {"form": form})

# def ShowLoginForm(req):
#     form = AuthenticationForm()
#     if req.POST:
#         print("Logining in User")
#         form = AuthenticationForm(req.POST)
#         uname = req.POST.get("username")
#         pword = req.POST.get("password")
#         print(uname, pword)
#         current_user = authenticate(username=uname, password=pword)
#         if current_user is not None:
#             print("Logged in successfully")
#             login(req, current_user)
#             messages.success(req, "Logged in successfully")
#             next_url = req.GET.get("next", "/")
#             return redirect(next_url)
#         else:
#             print("FAILED to Login")
#             messages.error(req, "FAILED to Login")
#             return redirect("/")

#     return render(req, "auth_app/login_form.html", {"form": form})
