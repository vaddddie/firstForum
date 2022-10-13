from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from django.contrib.auth.forms import\
    UserCreationForm,\
    AuthenticationForm,\
    PasswordResetForm,\
    SetPasswordForm,\
    PasswordChangeForm


class Registration_form(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form_label'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form_label'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_label'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form_label'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Login_form(AuthenticationForm):
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


class Password_reset_confirm_form(SetPasswordForm):
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={
        'class': 'form_label'
    }))

    new_password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={
        'class': 'form_label'
    }))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')

# ==============================================================

class Password_change_form(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={
        'class': 'form_label'
    }))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
        'class': 'form_label'
    }))
    new_password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={
        'class': 'form_label'
    }))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
