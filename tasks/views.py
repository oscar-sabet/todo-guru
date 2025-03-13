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


# @login_required
# def task_board(request):
#     order_by = request.GET.get("order_by", "status")  # Default ordering by status
#     tasks = Task.objects.filter(user=request.user).order_by(order_by)
#     not_started_tasks = tasks.filter(status="P")
#     in_progress_tasks = tasks.filter(status="IP")
#     completed_tasks = tasks.filter(status="C")
#     return render(
#         request,
#         "task/task_board.html",
#         {
#             "not_started_tasks": not_started_tasks,
#             "in_progress_tasks": in_progress_tasks,
#             "completed_tasks": completed_tasks,
#             "order_by": order_by,
#         },
#     )
