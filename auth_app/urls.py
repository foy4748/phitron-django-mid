from django.urls import path
from . import views


app_name = "auth"

urlpatterns = [
    # For Django Hard Reload
    path("register/", views.ShowRegistrationForm, name="registration_form"),
    path("login/", views.ShowLoginForm.as_view(), name="login_form"),
    path("logout/", views.LogoutUser, name="logout"),
    path(
        "password-change/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path("profile-change/", views.ChangeProfileView.as_view(), name="change_profile"),
]
