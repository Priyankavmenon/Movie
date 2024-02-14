from django import forms
from django.contrib.auth.models import User
from Myapp.models import Genre,Movie
class Register(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","first_name","last_name","email"]
class Login(forms.Form):
    username=forms.CharField()
    password=forms.CharField() 

class Genreform(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'
class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'