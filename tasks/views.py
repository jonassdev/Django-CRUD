from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.db import IntegrityError

from django.http import HttpResponse, HttpResponseServerError

from .forms import TaskForm
from .models import Tasks

from django.utils import timezone

from django.contrib.auth.decorators import login_required

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
    
# permite iniciar sesion con cuentas ya creadas (signin)
def signin(request):
    # Metodo GET

    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    # Metodo POST
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña es incorrecto'
            })
        else:
            # Informacion del Usuario. Guarda e inicia la sesion
            login(request, user)
            return redirect('tasks')

# cerrar sesion (logout - signout)
@login_required
def signout(request):
    logout(request)
    return redirect('home')


@login_required
def tasks(request):
    tasks = Tasks.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks,
        'tag' : 'Pending'
    })

@login_required
def tasks_completed(request):
    tasks = Tasks.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    show_datecompleted_column = any(task.datecompleted is not None for task in tasks)
    return render(request, 'tasks.html', {
        'tasks': tasks,
        'tag' : 'All',
        'show_datecompleted_column': show_datecompleted_column
    })

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form' : TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form' : TaskForm
            })
            
@login_required          
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Tasks, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html',{
            'task' : task,
            'form' : form
        })
    else:
        try:
            print(request.POST)
            task = get_object_or_404(Tasks, pk=task_id)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html',{
            'task' : task,
            'form' : form,
            'error' : 'Error al Actualizar Datos'
        })
            
@login_required           
def complete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    if request.method == 'POST':        
        task.delete()
        return redirect('tasks')