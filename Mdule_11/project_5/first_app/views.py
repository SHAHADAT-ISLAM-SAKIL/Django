from django.shortcuts import render

from .forms import contactForm
from .forms import StudentData , PasswordValidationProject


# Create your views here.
def index(request):
    
    if request.method == 'POST':
        name = request.POST.get('username')
        select = request.POST.get('select')
        email = request.POST.get('email')
        return render(request, 'index.html',{'name' : name, 'email':email, 'select' : select})
    else:
      return render(request, 'index.html')
  


def about(request ):
    return render(request, 'index.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        select = request.POST.get('select')
        email = request.POST.get('email')
        return render(request, 'index.html',{'name' : name, 'email':email, 'select' : select})
    else:
     return render(request, 'from.html')
    
def DjangoForm(request):
   
    if request.method == 'POST':
       form = contactForm(request.POST,request.FILES)
       if form.is_valid():
          file = form.cleaned_data['file']
          with open('./first_app/upload/' + file.name, 'wb+') as destination:
              for chunk in file.chunks():
                  destination.write(chunk)
          print(form.cleaned_data)
          return render(request, 'django_form.html', {'form':form})
    else:
          form = contactForm()

    return render(request, 'django_form.html', {'form':form})
       
         
def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, 'django_form.html', {'form': form})

   
def PassowardValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(request, 'django_form.html', {'form': form})

