from django.contrib import admin
from django.urls import path
from .views import task_list, task_create

urlpatterns = [
    path('tasks/', task_list, name='tasks'),
    path('task_create/', task_create, name='task_create'),
]