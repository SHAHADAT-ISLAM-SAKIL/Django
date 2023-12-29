from django import forms
from .models import AlbumInfo

class AlbumForm(forms.ModelForm):
    class Meta:  
        model = AlbumInfo
        fields = '__all__'