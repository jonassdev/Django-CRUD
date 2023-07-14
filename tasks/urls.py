
from django.contrib import admin
from django.urls import path
from tasks import views



urlpatterns = [
    path('' , views.home, name='home'),
    path('signup/' , views.signup , name='signup'),
    path('tasks/' , views.tasks , name='tasks'),
    path('logout/' , views.logout , name='logout'),
]
