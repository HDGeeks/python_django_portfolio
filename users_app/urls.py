from django.urls import URLPattern, path
from . import views as users_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', users_view.register, name='register'),
    path('profile/', users_view.profile, name='profile'),
    path('login/',
         auth_view.LoginView.as_view(template_name='users_app/login.html'),
         name='login'),
    path('logout',
         auth_view.LogoutView.as_view(template_name='users_app/logout.html'),
         name='logout'),
    path('password_reset',
         auth_view.PasswordResetView.as_view(
             template_name='users_app/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_view.PasswordResetDoneView.as_view(
             template_name='users_app/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(
             template_name='users_app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         auth_view.PasswordResetCompleteView.as_view(
             template_name='users_app/password_reset_complete.html'),
         name='password_reset_complete'),
]