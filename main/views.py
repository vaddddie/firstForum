from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.views import View
from django.views.generic import CreateView

from main.forms import RegistrationForm, LogInForm, Password_reset_form


class Index(View):
    template_name = 'main/homePage.html'

    context = {

    }

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class Registration(CreateView):
    form_class = RegistrationForm
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
    form_class = LogInForm
    template_name = 'main/registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self, **kwargs):
        return reverse("home")


def Logout(request):
    logout(request)
    return redirect('home')


class Password_reset_form_class(View):
    template_name = 'main/registration/password_reset_form.html'

    def post(self, request, *args, **kwargs):
        form_class = Password_reset_form(request.POST)
        if form_class.is_valid():
            data = form_class.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
        form_class = Password_reset_form(request.POST)
        context = {
            "form": form_class
        }
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        form_class = Password_reset_form()

        context = {
            "form": form_class
        }
        return render(request, self.template_name, context)

class Password_reset_done(View):
    template_name = 'main/registration/password_reset_done.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)