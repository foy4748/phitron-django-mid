"""
URL configuration for car_sales_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("", include("car.urls")),
    path("car_orders/", include("order_car.urls")),
    path("auth/", include("auth_app.urls")),
    path("comment/", include("comment.urls")),
    # Admin page
    path("admin/", admin.site.urls),
    # Test page
    path("test/", TemplateView.as_view(template_name="test.html"), name="test_page"),
]

# Adding Media Config URL at the end
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
