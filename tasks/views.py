from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm, LoginForm, RegistrationForm
from django.http import JsonResponse
from django.contrib.auth import login


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
    return render(request, "tasks/tasks.html", context)


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


@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.status = request.POST.get("status")
        task.save()
    return redirect("task_board")


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Set the user field
            task.save()
        return redirect("/tasks/")
    return redirect("/tasks/")


@login_required
def update_task(request, p_key):
    task = get_object_or_404(Task, id=p_key, user=request.user)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/tasks/")

    context = {"form": form}
    return render(request, "task/update_task.html", context)


@login_required
def delete_task(request, p_key):
    task = get_object_or_404(Task, id=p_key, user=request.user)
    if request.method == "POST":
        task.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "task/register.html", {"form": form})
