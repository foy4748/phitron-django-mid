from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from car.models import Car
from order_car.models import CarOrder
from django.contrib import messages

# Create your views here.


@login_required
def PlaceOrder(req, pk):
    car = Car.objects.get(pk=pk)
    user = req.user
    carOK = car is not None
    userOK = user is not None

    if carOK and userOK:
        car.quantity = car.quantity - 1
        car.save()
        newOrder = CarOrder(buyer_id=user, car_id=car)
        newOrder.save()
        print(newOrder)
        success_message = f"Place a new order: {car.brand} | {car.car_model}"
        messages.success(req, success_message)
        nextUrl = reverse("order_car:my_orders")
        return HttpResponseRedirect(nextUrl)
    else:
        error_message = f"Failed to order"
        messages.error(req, error_message)
        nextUrl = reverse("car:car_list")
        return HttpResponseRedirect(nextUrl)


class OrderList(LoginRequiredMixin, ListView):
    model = CarOrder
    template_name = "order_car/carorder_list.html"

    # Thanks to this stackoverflow page
    # https://stackoverflow.com/questions/38471260/django-filtering-by-user-id-in-class-based-listview

    def get_queryset(self):
        return CarOrder.objects.filter(buyer_id=self.request.user).order_by(
            "-order_date"
        )
