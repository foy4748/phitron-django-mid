from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.views.generic.list import ListView

from car.forms import AddBrandForm, AddCarForm
from car.models import Brand, Car

# Create your views here.


class ShowCarList(ListView):
    model = Car


class ShowCarAddForm(CreateView):
    model = Car
    form_class = AddCarForm
    success_url = reverse_lazy("car:car_list")

    def form_valid(self, form):
        print(form.cleaned_data)
        brand = form.cleaned_data["brand"]
        car_model = form.cleaned_data["car_model"]
        success_message = f"Added a new car: {brand} | {car_model}"
        messages.success(self.request, success_message)

        return super().form_valid(form)


class ShowBrandAddForm(CreateView):
    model = Brand
    form_class = AddBrandForm
    success_url = reverse_lazy("car:car_list")

    def form_valid(self, form):
        brand = form.cleaned_data["brand_name"]
        success_message = f"Added a new brand: {brand}"
        messages.success(self.request, success_message)

        return super().form_valid(form)
