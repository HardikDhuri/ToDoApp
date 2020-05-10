from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect(reverse('index'))
    context ={
        'form':form,
        'tasks':tasks,
    }
    return render(request, "tasks/index.html", context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form  = TaskForm(instance=task)
    if request.method == "POST":
        form  = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
        return redirect(reverse("index"))

    context = {
        'task': task,
        'form': form,
    }
    return render(request, "tasks/update.html", context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect(reverse("index"))
        
    context = {
        'task': task,
    }
    return render(request, "tasks/delete.html", context)
    