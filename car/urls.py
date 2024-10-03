from django.urls import path

# from django.views.generic import TemplateView

from . import views

app_name = "car"

urlpatterns = [
    path("", views.ShowCarAndBrandList, name="car_list"),
    path("car-detail/<str:pk>/", views.ShowCarDetail.as_view(), name="car_detail"),
    path("add_car/", views.ShowCarAddForm.as_view(), name="add_car_form"),
    path("add_brand/", views.ShowBrandAddForm.as_view(), name="add_brand_form"),
]
