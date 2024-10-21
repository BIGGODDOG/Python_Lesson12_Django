from django import forms
from .models import Car, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_year(self):
        year = self.cleaned_data["year"]
        if year > datetime.now().year:
            raise forms.ValidationError("Ваш год из будущего")
        return year

    
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"