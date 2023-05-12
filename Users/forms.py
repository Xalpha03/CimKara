from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LogupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pwd1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pwd2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))