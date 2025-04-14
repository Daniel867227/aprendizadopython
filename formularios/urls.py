from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('usuarios', views.usuarios, name='usuarios'),
    path('edit_usuarios/<usuarios_id>', views.edit_usuarios, name='edit_usuarios'),

]
