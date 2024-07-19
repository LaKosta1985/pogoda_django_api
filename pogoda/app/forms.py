from django import forms
from .models import *

class City_Form(forms.Form):
    name_City = forms.CharField(min_length=2,max_length=30,label="Введите название города:")
  