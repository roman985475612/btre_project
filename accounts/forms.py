from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', max_length=100)
    confirm_password = forms.CharField(label='Confirm password', max_length=100)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('That username is taken')
        return self.cleaned_data['username']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('That email is being used')
        return self.cleaned_data['email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            msg = 'Password do not match!'
            self.add_error('password', msg)
            self.add_error('confirm_password', msg)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
