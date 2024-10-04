from django.urls import path

from . import views

app_name = "comment"

urlpatterns = [
    path(
        "add-comment/<str:car_id>/<str:user_id>",
        views.CreateComment.as_view(),
        name="add_comment",
    ),
]
