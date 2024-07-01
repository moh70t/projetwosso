from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, initial=1)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nom')
    lastname = forms.CharField(max_length=100, label='Prenom')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Votre Message')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user