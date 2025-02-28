from django.shortcuts import render, redirect
from .models import Management
from datetime import date


def task_list(request):
    tasks = Management.objects.all()

    for task in tasks:
        if task.due_date < date.today() and task.status != "Overdue":
            task.status = "Overdue"
            task.save()

    return render(request, 'task_list.html', {'tasks': tasks})
# I put conditional statement here to satisfy the condition that if the date is less than the current date, it will be marked as overdue.

def task_create(request):
    return render(request, 'task_form.html')

def task_update(request, task_id):
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

def task_delete(request, task_id):
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