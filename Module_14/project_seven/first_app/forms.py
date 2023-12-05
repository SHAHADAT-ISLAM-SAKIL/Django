from django import forms 
from first_app.models import StudentModels
# from . models import StudentModels

class StudentForm(forms.ModelForm):
    class Meta :
        model = StudentModels
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['roll']
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll',
        }
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'btn-primary'}),

         }
        help_texts = {
            'name' : "write your full name"
        }

        error_messages = {
            'name' : {'required' : 'your name is required'}
        }
