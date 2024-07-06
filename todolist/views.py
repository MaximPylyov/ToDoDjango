from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/index.html', {'task_list': tasks, 'title': 'Главаня страница'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    task = Task(title=title)
    task.save()
    return redirect('index')


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_complete= not task.is_complete
    task.save()
    return redirect('index')


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')