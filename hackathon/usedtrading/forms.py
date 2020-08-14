from django import forms
from .models import Usedtrading

class UsedtradingUpdate(forms.ModelForm):
    class Meta:
        model = Usedtrading
        fields = ['title','body','cost','images','image2','image3']