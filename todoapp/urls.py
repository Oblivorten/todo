from django.contrib import admin
from django.urls import path
from .views import task_list, task_create, task_details

urlpatterns = [
    path('tasks/', task_list, name='tasks'),
    path('task_create/', task_create, name='task_create'),
    path('task_details/ <int:task_id>', task_details, name='task_details'),
]