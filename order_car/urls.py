from django.urls import path
from django.views.generic import TemplateView

app_name = "order_car"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
]
