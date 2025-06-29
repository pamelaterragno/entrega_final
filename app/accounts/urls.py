from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    
    #editar perfil y cambiar clave
    path('edit_profile/', views.edit_profile, name='editar_perfil'),
    path('change_password/', PasswordChangeView.as_view(template_name='change_password.html', success_url='/'), name='change_password'),
]
