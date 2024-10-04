from django import forms

from comment.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = (
            "user",
            "car",
            "createdAt",
        )
