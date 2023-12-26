from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class RegisterForm(UserCreationForm):
    # ekhan theke requierd add korar jono nicher egula alada kore likhechi shate forms ke import korechi
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    # end requierd
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email']
