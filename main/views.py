from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import\
    LoginView,\
    LogoutView,\
    PasswordResetView,\
    PasswordResetDoneView,\
    PasswordResetConfirmView,\
    PasswordResetCompleteView

from main.forms import\
    Registration_form,\
    Login_form,\
    Password_reset_form,\
    Password_reset_confirm_form,\
    Password_change_form

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView


class Index(View):
    template_name = 'main/homePage.html'

    context = {

    }

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

# =============================== Registration =============================== #

class Registration(CreateView):
    form_class = Registration_form
    template_name = 'main/registration/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_success_url(self, **kwargs):
        return reverse("home")


class Login(LoginView):
    form_class = Login_form
    template_name = 'main/registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self, **kwargs):
        return reverse("home")


class Logout(LogoutView):
    pass


class Password_reset(PasswordResetView):
    form_class = Password_reset_form
    email_template_name = 'main/registration/password_reset_email.html'
    template_name = 'main/registration/password_reset_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Password_reset_done(PasswordResetDoneView):
    template_name = 'main/registration/password_reset_done.html'


class Password_reset_confirm(PasswordResetConfirmView):
    form_class = Password_reset_confirm_form
    template_name = 'main/registration/password_reset_confirm.html'


class Password_reset_complete(PasswordResetCompleteView):
    template_name = 'main/registration/password_reset_complete.html'


# =============================== Registration =============================== #
