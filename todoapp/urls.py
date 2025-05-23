from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import task_list, task_create, task_details, task_delete, task_update, register


urlpatterns = [
    path('tasks/', task_list, name='tasks'),
    path('task_create/', task_create, name='task_create'),
    path('task_details/<int:task_id>', task_details, name='task_details'),
    path('task_delete/<int:task_id>', task_delete, name='task_delete'),
    path('', task_list, name='tasks'),
    path('task_update/<int:task_id>', task_update, name='task_update'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]