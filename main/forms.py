from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    lastname = forms.CharField(max_length=100, label='LastName')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Email address invalide.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )