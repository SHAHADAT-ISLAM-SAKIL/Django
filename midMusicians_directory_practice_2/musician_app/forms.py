from django import forms
from .models import MusicianInfo
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MusicianForm(forms.ModelForm):
    class Meta:  
        model = MusicianInfo
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']