from django.shortcuts import render
from . forms import Usuarios_form
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import Usuarios

def index(request):
    if request.method != 'POST':
        form = Usuarios_form()
    else:
        form = Usuarios_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    
    contexto = {'form': form}
    return render(request, 'formularios/index.html', contexto)


def usuarios(request):
    usuarios = Usuarios.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request,'formularios/usuarios.html', contexto)


def edit_usuarios(request, usuarios_id ):
    usuario = Usuarios.objects.get(id= usuarios_id)

    if request.method != 'POST':
        form = Usuarios_form(instance=usuario)

    else:
        form = Usuarios_form(instance=usuario, data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('usuarios'))
    
    contexto = {'usuario': usuario, 'form': form}

    return render (request, 'formularios/edit_usuarios.html', contexto)
