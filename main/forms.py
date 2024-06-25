from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='')
    username = forms.CharField(max_length=30, help_text='')
    first_name = forms.CharField(max_length=30, label='Nom')
    last_name = forms.CharField(max_length=30, label='Prenom')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')