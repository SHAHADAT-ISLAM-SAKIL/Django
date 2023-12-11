from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

def add_task(request):
    if request.method == 'POST':
        post_form = TaskForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('show_tasks')
    else:
        post_form = TaskForm()
    return render(request, 'add_task.html', {'form': post_form})

def edit_task(request, task_id):
    post = TaskModel.objects.get(pk=task_id)
    post_form = TaskForm(instance=post)

    if request.method == 'POST':
        post_form = TaskForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('show_tasks')

    return render(request, 'add_task.html', {'form': post_form, 'post_id': task_id})

def delete_task(request, task_id):
    post = TaskModel.objects.get(pk=task_id)
    post.delete()
    return redirect('show_tasks')

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})
