from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('registration/', views.Registration.as_view(), name="registration"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password_reset/form/', views.Password_reset.as_view(), name='password_reset'),
    path('password_reset/done/', views.Password_reset_done.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>', views.Password_reset_confirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete', views.Password_reset_complete.as_view(), name='password_reset_complete'),
]
