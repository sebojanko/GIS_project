from django import forms
from .models import Point


class PointForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = ('name', 'coordinate_x', 'coordinate_y')