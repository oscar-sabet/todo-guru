from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm


# Create your views here.
@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by("-status", "-created")
    form = TaskForm()

    # Calculate the time taken and time until due date for each task
    for task in tasks:
        if task.completed_date:
            task.time_taken = task.completed_date - task.created
            task.elapsed_time = None
        else:
            task.elapsed_time = timezone.now() - task.created
            task.time_taken = None

        if task.due_date:
            task.time_until_due = task.due_date - timezone.now()
        else:
            task.time_until_due = None

    context = {"tasks": tasks, "form": form}
    return render(request, "task/tasks.html", context)
