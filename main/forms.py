from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form_label'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form_label'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_label'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form_label'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LogInForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form_label'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_label'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class Password_reset_form(PasswordResetForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form_label'}))

    class Meta:
        model = User
        fields = 'email'

