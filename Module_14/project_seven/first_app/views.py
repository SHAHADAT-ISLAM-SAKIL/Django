from django.shortcuts import render
from first_app.forms import StudentForm

def home(request):
    form = StudentForm()  # Initialize the form outside the if block
    if request.method == 'POST':  # Correct 'post' to 'POST'
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            # Add further processing for the form data if needed
        # Handling for invalid form data can be added here
    return render(request, 'home.html', {'form': form})