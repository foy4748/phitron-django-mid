from django.urls import path

from . import views

app_name = "order_car"

urlpatterns = [
    path("place-order/<str:pk>/", views.PlaceOrder, name="place_order"),
    path("my-orders/", views.OrderList.as_view(), name="my_orders"),
]
