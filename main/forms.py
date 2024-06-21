from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nom')
    lastname = forms.CharField(max_length=100, label='Prenom')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Votre Message')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='')
    username = forms.CharField(max_length=30, help_text='')
    first_name = forms.CharField(max_length=30, label='Nom')
    last_name = forms.CharField(max_length=30, label='Prenom')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')