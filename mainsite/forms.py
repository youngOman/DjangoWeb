from django.forms.widgets import PasswordInput, TextInput
from mainsite.models import User
from django import forms
class Loginform(forms.Form):
    account=forms.CharField(label="account", max_length=25, required=True,widget=forms.TextInput(attrs={'placeholder':'帳號...'}))
    password=forms.CharField(label="password", max_length=20,required=True,widget=forms.PasswordInput(attrs={'placeholder':'密碼...'}))