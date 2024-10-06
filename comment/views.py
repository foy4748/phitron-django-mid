# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from car.models import Car
from comment.models import Comment
from .forms import AddCommentForm

# Create your views here.


class CreateComment(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = "comment/comment_form.html"

    def get_success_url(self):
        return reverse_lazy("car:car_detail", kwargs={"pk": self.kwargs["car_id"]})

    def form_valid(self, form):
        print(self.kwargs["car_id"])
        comment = form.save(commit=False)
        car = get_object_or_404(Car, pk=self.kwargs["car_id"])
        user = self.request.user
        carOK = car is not None
        userOK = user is not None
        if carOK and userOK:
            comment.user = user
            comment.car = car
            comment.save()
        return super().form_valid(form)
