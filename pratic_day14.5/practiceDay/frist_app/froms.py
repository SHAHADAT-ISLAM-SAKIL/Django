
# from django import forms  
# from .models import GeeksModel   
# # creating a form   
# class InputForm(forms.Form):  
    
#     first_name = forms.CharField(max_length = 200)  
#     last_name = forms.CharField(max_length = 200)  
#     roll_number = forms.IntegerField(  
#                      help_text = "Enter 6 digit roll number"
#                      )  
#     password = forms.CharField(widget = forms.PasswordInput()) 
 
# class GeeksForm(forms.ModelForm): 
#     # specify the name of model to use 
#     class Meta: 
#         model = GeeksModel 
#         fields = "__all__"

from django import forms
from django.forms.widgets import NumberInput
import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ExampleForm(forms.Form):
          
          name = forms.CharField()
          comment = forms.CharField(widget=forms.Textarea)
          comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
          email = forms.EmailField()
          agree = forms.BooleanField()
          date = forms.DateField()
          birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
          value = forms.DecimalField()
          email_address = forms.EmailField( required = False,)
          message = forms.CharField(max_length = 10,)
          email_address = forms.EmailField( label="Please enter your email address",)  
          first_name = forms.CharField(initial='Your name')
          agree = forms.BooleanField(initial=True)
          day = forms.DateField(initial=datetime.date.today)
          favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
          favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
          favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
