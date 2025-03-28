from django.shortcuts import render
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    template = 'todoapp/task_list.html'
    context = {
        'tasks': tasks
    }
    return render(request, template, context)

