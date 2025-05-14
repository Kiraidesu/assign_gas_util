from django import forms
from .models import ServiceRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")