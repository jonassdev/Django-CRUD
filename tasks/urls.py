
from django.contrib import admin
from django.urls import path
from tasks import views



urlpatterns = [
    path('' , views.home, name='home'),
    path('signup/' , views.signup , name='signup'),
    path('signup/' , views.signup , name='signup'),
    path('logout/' , views.signout , name='logout'),
    path('signin/' , views.signin , name='signin'),
    path('tasks/' , views.tasks , name='tasks'),
    path('tasks/create/' , views.create_task , name='create_task'),
    path('tasks/<int:task_id>/' , views.task_detail , name='task_detail'),
    
]
