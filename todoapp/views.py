from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    template = 'todoapp/task_list.html'
    context = {
        'tasks': tasks
    }
    return render(request, template, context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    template = 'todoapp/task_create.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def task_details(request, task_id):
    template = 'todoapp/task_details.html'
    task = get_object_or_404(Task, id=task_id)
    context = {
        'task': task
    }
    return render(request, template, context)


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return redirect('tasks')