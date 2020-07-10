from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(label="İsim", max_length=25, widget=forms.TextInput(attrs={'placeholder': 'İsim'}))
    last_name = forms.CharField(label="Soyisim", max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Soyisim'}))
