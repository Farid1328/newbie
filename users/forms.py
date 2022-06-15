from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {
            'username':TextInput(attrs={
                'class':"form-control",
                'style':"max-width: 300px;",
                'placeholder':'username'
            })
        }


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude =['owner']