from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('registration/', views.Registration.as_view(), name="registration"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout, name='logout'),
    path('password_reset/form/', views.Password_reset_form_class.as_view(), name='password_reset'),
    path('password_reset/done/', views.Password_reset_done.as_view(), name='password_reset_done'),


]
