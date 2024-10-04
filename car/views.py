from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib import messages

from car.forms import AddBrandForm, AddCarForm
from car.models import Brand, Car
from comment.forms import AddCommentForm

# Create your views here.


def ShowCarAndBrandList(req):
    brand_list = Brand.objects.all()
    brand_id = req.GET.get("brand_id")

    is_filtered = False
    brand = None

    if brand_id is None:
        car_list = Car.objects.all()
    else:
        brand = Brand.objects.get(id=brand_id)
        car_list = Car.objects.filter(brand=brand)
        is_filtered = True

    ctx = {
        "car_list": car_list,
        "brand_list": brand_list,
        "is_filtered": is_filtered,
        "brand": brand,
    }
    return render(req, "car/car_list.html", context=ctx)


class ShowCarAddForm(LoginRequiredMixin, CreateView):
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


class ShowBrandAddForm(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = AddBrandForm
    success_url = reverse_lazy("car:car_list")

    def form_valid(self, form):
        brand = form.cleaned_data["brand_name"]
        success_message = f"Added a new brand: {brand}"
        messages.success(self.request, success_message)

        return super().form_valid(form)


class ShowCarDetail(DetailView, CreateView):
    model = Car
    context_object_name = "car"
    template_name = "car/car_detail.html"
    form_class = AddCommentForm

    # Thanks to Co-pilot
    # For Returning the Form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["pk"] = self.kwargs["pk"]
        return context
