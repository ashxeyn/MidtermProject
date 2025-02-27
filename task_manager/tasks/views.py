from django.shortcuts import render, redirect
from .models import Management
from datetime import date


def index(request):
    tasks = Management.objects.all()

    for task in tasks:
        if task.due_date < date.today() and task.status != "Overdue":
            task.status = "Overdue"
            task.save()

    return render(request, 'index.html', {'tasks': tasks})

def addTask(request):
    return render(request, 'task_form.html')

def editTask(request, task_id):
    task = Management.objects.get(id=task_id)
    return render(request, 'task_form.html', {'task': task})

def update(request):
    task_id = request.POST.get('task_id')
    title = request.POST.get('title')
    description = request.POST.get('description')
    status = request.POST.get('status')
    due_date = request.POST.get('due_date')

    task = Management.objects.get(id=task_id)
    task.title = title
    task.description = description
    task.due_date = due_date
    task.status = status
    task.save()
    return redirect('/tasks/')

def deleteTask(request, task_id):
    task = Management.objects.get(id=task_id)
    return render(request, 'task_confirm_delete.html', {'task': task})

def delete(request):
    task_id = request.POST.get('task_id')
    
    task = Management.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')

def submit(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    due_date = request.POST.get('due_date')
    new_management = Management(title=title, description=description, due_date=due_date)
    new_management.save()
    return redirect('/tasks/')