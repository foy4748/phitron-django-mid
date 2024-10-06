from django import forms

from comment.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {"commenter_name": "Your Name"}
        # fields = "__all__"
        exclude = (
            "car",
            "createdAt",
        )
