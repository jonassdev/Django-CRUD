from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.db import IntegrityError

from django.http import HttpResponse, HttpResponseServerError


# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# Crear cuenta nueva


def signup(request):
    # Metodo POST
    if request.method == "POST":
        print(request.POST)
        print("obteniendo datos")
        if request.POST['password1'] == request.POST['password2']:
            # Registrar Usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # Informacion del Usuario. Guarda la sesion
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'response': 'Usuario Ya Existe',
                    'form': UserCreationForm
                })
        else:
            return render(request, 'signup.html', {
                'response': 'No coinciden las contraseñas',
                'form': UserCreationForm
            })
    # Metodo GET
    else:
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

# cerrar sesion


def signout(request):
    logout(request)
    return redirect('home')

# permite iniciar sesion con cuentas ya creadas


def signin(request):
    # Metodo GET

    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña es incorrecto'
            })
        else:
            # Informacion del Usuario. Guarda la sesion
            
            login(request, user)
            return redirect('tasks')


def tasks(request):
    return render(request, 'tasks.html')
