from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
                return render(request, 'signup.html', {
                    'response': 'Usuario registrado correctamente',
                    'form': UserCreationForm
                })
            except:
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
