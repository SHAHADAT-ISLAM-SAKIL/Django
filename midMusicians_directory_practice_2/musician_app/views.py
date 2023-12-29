from django.shortcuts import render, redirect
from .forms import MusicianForm
from .forms import MusicianInfo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required  
from . import models 
from . import forms


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.RegistrationForm() 

    return render(request, 'register.html', {'form': form, 'type': 'Sign'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request =request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user-name']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form':form, 'type':'Log'})




@login_required 
def add_Musician(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            musician_form = MusicianForm(request.POST)
            if musician_form.is_valid():
                musician_form.save()
                return redirect('home')
        else:
            musician_form = MusicianForm()

        return render(request, 'Musician.html', {'form': musician_form})
    else:
       
        return redirect('register') 




@login_required 
def edit_Musician(request, id):
    musician = models.MusicianInfo.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)

    if request.method == "POST":
        musician_form = MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
   
    return render(request, 'musician.html', {'form': musician_form})

@login_required 
def delete_musician(request, id):
    musician = models.MusicianInfo.objects.get(pk=id)
    musician.delete()
    return redirect('home')

def user_logout(request):
    logout(request)
    return redirect('register')