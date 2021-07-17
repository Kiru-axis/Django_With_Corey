from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/",views.register,name = "users-register"),
    path("login/",auth_views.LoginView.as_view,name = "users-login"),
    path("register/",auth_views.LogoutView.as_view(),name = "users-logout"),
]