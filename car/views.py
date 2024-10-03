from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib import messages
from django.views.generic.list import ListView

from car.forms import AddCarForm
from car.models import Car

# Create your views here.


class ShowCarList(ListView):
    model = Car


class ShowCarAddForm(CreateView):
    model = Car
    form_class = AddCarForm
    success_url = "/"

    def form_valid(self, form):
        brand = form.cleaned_data.brand_name
        car_model = form.cleaned_data.car_model
        success_message = f"Added a new car: {brand} | {car_model}"
        messages.success(self.request, success_message)

        return super().form_valid(form)
