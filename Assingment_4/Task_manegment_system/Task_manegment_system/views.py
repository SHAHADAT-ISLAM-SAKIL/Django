from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

# Other views related to the main project can be added here
