from django.shortcuts import render , redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , SetPasswordForm
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.http import HttpResponse

# Create your views here.

def base(request):
   return render(request, 'base.html')


def singup(request):
   if not request.user.is_authenticated:
      if request.method== 'POST':
         form = RegisterForm(request.POST)
         if form.is_valid():
            messages.success(request,'Account created successfully!')
            form.save()
            print(form.cleaned_data)
      else :
         form = RegisterForm()
      return render(request, 'singup.html', {'form': form})
   else:
      return redirect('profile')  # Redirect to profile if the user is already authenticated
    
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)

                if user is not None:
                    login(request, user)
                    return redirect('profile')

            messages.error(request, 'Invalid credentials. Please try again.')
            form = AuthenticationForm()  # Create a new form after an error
            return render(request, 'login.html', {'form': form})
        
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    return redirect('profile')  # Redirect to profile if the user is already authenticated

def profile(request):
   if  request.user.is_authenticated:
         if request.method== 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
               messages.success(request,'Account Update successfully!')
               form.save()
               print(form.cleaned_data)
         else :
            form = ChangeUserData(instance = request.user)
         return render(request, 'profile.html', {'form': form})
   else:
         return redirect('singup')  # Redirect to profile if the user is already authenticated
def user_logout( request):
   logout(request)
   return redirect('login')

def passchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Update the session after password change
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password.html', {'form': form})

def passchange2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Update the session after password change
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'password.html', {'form': form})


def change_user_data(request):
   if  request.user.is_authenticated:
      if request.method== 'POST':
         form = ChangeUserData(request.POST, instance = request.user)
         if form.is_valid():
            messages.success(request,'Account Update successfully!')
            form.save()
            print(form.cleaned_data)
      else :
         form = ChangeUserData()
      return render(request, 'profile.html', {'form': form})
   else:
      return redirect('singup')  # Redirect to profile if the user is already authenticated