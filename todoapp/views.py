from django.shortcuts import render


def task_list(request):
    return render(request, 'todoapp/task_list.html')
