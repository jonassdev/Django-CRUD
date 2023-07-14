from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.db import IntegrityError

from django.http import HttpResponse, HttpResponseServerError


# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# Signup


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
                # Informacion del Usuario
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

def tasks(request):
    return render(request, 'tasks.html')

def logout(request):
    return render(request, 'logout.html')