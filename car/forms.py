from django import forms

from car.models import Brand, Car


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class AddBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
