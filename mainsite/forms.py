from django import forms
class Loginform(forms.Form):
    account=forms.CharField(label="account", max_length=25, required=True)
    password=forms.CharField(label="password", max_length=20,required=True,widget=forms.PasswordInput)
    email=forms.EmailField(label='email', required=False)