from django.shortcuts import render, get_object_or_404
from . forms import Usuarios_form
from . models import Usuarios
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.urls import reverse


def index(request):
    if request.method != 'POST':
        form = Usuarios_form()
    else:
        form = Usuarios_form(request.POST)
        if form.is_valid():
            form.save()
            frase = 'Usario Cadastrado com sucesso'
            contexto = {'form':form, 'frase':frase}
            return render(request, 'formularios/index.html', contexto)
        
    contexto = {'form': form}
    return render(request, 'formularios/index.html', contexto)


def usuarios(request):
    usuarios = Usuarios.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'formularios/usuarios.html', contexto)


def edit_usuarios(request, usuarios_id):
    usuario = Usuarios.objects.get(id=usuarios_id)

    print(usuario)
    if not usuario:
        return HttpResponseNotFound(request, 'Não encontrada')

    if request.method != 'POST':
        form = Usuarios_form(instance=usuario)

    else:
        form = Usuarios_form(instance=usuario, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('usuarios'))

    contexto = {'usuario': usuario, 'form': form}

    return render(request, 'formularios/edit_usuarios.html', contexto)

def delete_usuarios(request, usuarios_id):
 
    usuario = Usuarios.objects.get(id= usuarios_id)
    usuario.delete()
    return HttpResponseRedirect(reverse('usuarios'))
    