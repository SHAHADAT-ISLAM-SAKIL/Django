
# django te from 2 doroner hoi :
# 1. form API : eta holo amra code korbo python er class e eta rendal (convert) hoye hoye jabe HTML format
# 2. mofel form 

from django.core import validators
from django import forms
 #ekhane forms ta holo django er from er API

# widgets == field to html input 
class contactForm(forms.Form):
    # name = forms.CharField(label="User Name :", initial = "shahadat" , help_text = "Total length must be  within70 characters", required= False, disabled= True )
    # Name2 = forms.CharField(label="User Name 2 :", initial = "shahadat" , help_text = "Total length must be  within70 characters", widget = forms.Textarea(attrs= {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : "Enter your name"}) )
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # age = forms.CharField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # birthday = forms.CharField(widget= forms.DateTimeInput(attrs= {'type' : 'date'}))
     # appointment = forms.DateTimeField()
    # appointment = forms.CharField(widget= forms.DateInput(attrs={'type': 'datetime-local'}))
    # # upload = forms.FileField()
    # CHOICES = [('s','Small'), ('M', 'Medium'), ('L','large')]
    # size = forms.ChoiceField(choices = CHOICES) 
    # size = forms.MultipleChoiceField(choices = CHOICES, widget= forms.RadioSelect) 

    # meal = [('p', 'Pepperoni'), ('M', 'Masroom'), ('B','Beef')]
    # pizza = forms.MultipleChoiceField(choices= meal)

    # pizza = forms.MultipleChoiceField(choices= meal, widget= forms.CheckboxSelectMultiple) 

    # name = forms.CharField(label = " User Name")
    # file = forms.FileField(label = 'file')
    pass

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # <-- def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("enter a name with al least 10 charcters")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in  valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail -->

    # def clean(self):
    #   clean_data = super().clean()
     
    #   valname = self.cleaned_data['name']
    #   valemail = self.cleaned_data['email']
    #   if '.com' not in  valemail:
    #           raise forms.ValidationError("Your email must contain .com")

    #   if len(valname) < 10:
    #           raise forms.ValidationError("enter a name with al least 10 charcters")
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter value at last 10 chars")

class StudentData(forms.Form):
    name = forms.CharField( validators=[validators.MaxLengthValidator(10,message="enter a name with at max 10 charcters")])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.MaxLengthValidator(10,message="enter a valid Email")])
    age = forms.IntegerField(validators= [
        validators.MaxValueValidator(34, message="age must be maximum 34"), validators.MinValueValidator(24, message="age must be at last 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message = "File Extension must be ended with .pdf")])
    # Regex, url egula niye o kaj kora jai

class PasswordValidationProject(forms.Form):
    name  = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

#jokhon multiple jinis nije kaj korbo tokhon clean method use korbo and cleaned_data = super().clean() use korbo.
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_compass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_compass != val_pass:
            raise forms.ValidationError('Passwords do not match.')
        if len(val_name) >20:
            raise forms.ValidationError("Name maxmimum length 20 characters")

    