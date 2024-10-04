# from django.shortcuts import render
from django.views.generic import CreateView

from comment.models import Comment
from .forms import AddCommentForm

# Create your views here.


class CreateComment(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = "comment/comment_form.html"

    def form_valid(self, form):
        return super().form_valid(form)
