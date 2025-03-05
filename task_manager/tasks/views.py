from django.shortcuts import render, redirect
from .models import Task
from django.db.models import Q
from datetime import datetime

# Create your views here.

def task_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = Task.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    else:
        tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date_str = request.POST.get('due_date')
        status = request.POST.get('status')
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status
        )
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_update(request, id):
    try:
        task = Task.objects.get(id=id)
        if request.method == 'POST':
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            due_date_str = request.POST.get('due_date')
            task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            task.save()
            return redirect('task_list')
        return render(request, 'task_form.html', {'task': task})
    except Task.DoesNotExist:
        return redirect('task_list')

def task_delete(request, id):
    try:
        task = Task.objects.get(id=id)
        if request.method == 'POST':
            task.delete()
            return redirect('task_list')
        return render(request, 'task_confirm_delete.html', {'task': task})
    except Task.DoesNotExist:
        return redirect('task_list')
