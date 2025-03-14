from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm, LoginForm, RegistrationForm
from django.http import JsonResponse
from django.contrib.auth import login

from django.contrib import messages


@login_required
def list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-status", "-created")
    form = TaskForm()

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
    return render(request, "tasks/list.html", context)


@login_required
def board(request):
    order_by = request.GET.get("order_by", "status")  # Default ordering by status
    tasks = Task.objects.filter(user=request.user).order_by(order_by)
    not_started_tasks = tasks.filter(status="P")
    in_progress_tasks = tasks.filter(status="IP")
    completed_tasks = tasks.filter(status="C")
    return render(
        request,
        "tasks/board.html",
        {
            "not_started_tasks": not_started_tasks,
            "in_progress_tasks": in_progress_tasks,
            "completed_tasks": completed_tasks,
            "order_by": order_by,
        },
    )


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
            messages.success(request, "Task created successfully.")
        else:
            messages.error(request, "Failed to create task.")
        return redirect("list")
    return redirect("list")


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated successfully.")
            return redirect("list")
        else:
            messages.error(request, "Failed to update task.")
            return redirect("list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/update_task.html", {"form": form, "task": task})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.status = "C" if request.POST.get("completed") else "P"
        task.save()
        messages.success(request, "Task status updated successfully.")
    return redirect("list")


@login_required
def delete_task(request, p_key):
    task = get_object_or_404(Task, id=p_key, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return JsonResponse({"success": True})
    messages.error(request, "Failed to delete task.")
    return JsonResponse({"success": False})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Registration failed.")
    else:
        form = RegistrationForm()
    return render(request, "task/register.html", {"form": form})
