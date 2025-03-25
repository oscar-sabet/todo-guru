from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task, Profile
from .forms import TaskForm, RegistrationForm, ProfileForm
from django.contrib.auth import login
from django.contrib import messages


@login_required
def list(request):
    """
    Display a list of tasks for the logged-in user, with sorting and filtering
    options.

    This view handles the display of tasks for the currently logged-in user.
    It supports sorting by various fields, filtering by status, category, and
    priority and calculates various statistics about the tasks.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of tasks and
        statistics.
    """
    sort_by = request.GET.get("sort", "created")
    sort_direction = request.GET.get("direction", "asc")
    status_filter = request.GET.get("status")
    category_filter = request.GET.get("category")
    priority_filter = request.GET.get("priority")
    valid_sort_fields = [
        "status",
        "category",
        "priority",
        "due_date",
        "created"
        ]

    if sort_by not in valid_sort_fields:
        sort_by = "created"

    if sort_direction == "desc":
        sort_by = f"-{sort_by}"

    tasks = Task.objects.filter(user=request.user)

    tasks.count = tasks.count()
    tasks.completed_tasks = tasks.filter(status="C").count()
    tasks.pending_tasks = tasks.filter(status="P").count()
    tasks.in_progress_tasks = tasks.filter(status="IP").count()
    tasks.low_priority_tasks = tasks.filter(priority="L").count()

    completed_tasks = tasks.filter(status="C").count()
    pending_tasks = tasks.filter(status="P").count()
    in_progress_tasks = tasks.filter(status="IP").count()

    low_priority_tasks = tasks.filter(priority="L").count()
    medium_priority_tasks = tasks.filter(priority="M").count()
    high_priority_tasks = tasks.filter(priority="H").count()

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if category_filter:
        tasks = tasks.filter(category=category_filter)
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    tasks = tasks.order_by(sort_by)
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

    context = {
        "tasks": tasks,
        "form": form,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "in_progress_tasks": in_progress_tasks,
        "low_priority_tasks": low_priority_tasks,
        "medium_priority_tasks": medium_priority_tasks,
        "high_priority_tasks": high_priority_tasks,
    }
    return render(request, "tasks/list.html", context)


@login_required
def board(request):
    """
    Display a board view of tasks for the logged-in user, categorized by
    status.

    This view handles the display of tasks for the currently logged-in user in
    a board format.
    Tasks are categorized by their status (not started, in progress,
    completed) and can be ordered by a specified field.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the board view of
        tasks.
"""
    order_by = request.GET.get("order_by", "status")
    tasks = Task.objects.filter(user=request.user).order_by(order_by)
    not_started_tasks = tasks.filter(status="P")
    in_progress_tasks = tasks.filter(status="IP")
    completed_tasks = tasks.filter(status="C")
    total_tasks = tasks.count()

    return render(
        request,
        "tasks/board.html",
        {
            "not_started_tasks": not_started_tasks,
            "in_progress_tasks": in_progress_tasks,
            "completed_tasks": completed_tasks,
            "order_by": order_by,
            "total_tasks": total_tasks,
        },
    )


@login_required
def update_task_status(request, task_id):
    """
    Update the status of a specific task for the logged-in user.

    This view handles updating the status of a specific task for the currently
    logged-in user. The new status is provided via a POST request.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to be updated.

    Returns:
        HttpResponseRedirect: Redirects to the board view after updating the
        task status.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.status = request.POST.get("status")
        task.save()
    return redirect("board")


@login_required
def create_task(request):
    """
    Create a new task for the logged-in user.

    This view handles the creation of a new task for the currently logged-in
    user. The task details are provided via a POST request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the list view after creating the
        task.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.status = "P"
            task.save()
            messages.success(request, "Task created successfully.")
        else:
            for error in form.errors.values():
                messages.error(request, error)
        return redirect("list")
    return redirect("list")


@login_required
def update_task(request, task_id):
    """
    Update an existing task for the logged-in user.

    This view handles updating an existing task for the currently logged-in
    user. The task details are provided via a POST request.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to be updated.

    Returns:
        HttpResponse: The rendered HTML page for updating the task.
        HttpResponseRedirect: Redirects to the list view after updating the
        task.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect("list")
        else:
            for error in form.errors.values():
                messages.error(request, error)
            return redirect("list")
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        "tasks/update_task.html",
        {"form": form, "task": task}
        )


@login_required
def complete_task(request, task_id):
    """
    Mark a task as completed or pending for the logged-in user.

    This view handles marking a specific task as completed or pending for the
    currently logged-in user. The new status is provided via a POST request.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to be updated.

    Returns:
        HttpResponseRedirect: Redirects to the list view after updating the
        task status.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.status = "C" if request.POST.get("completed") else "P"
        task.save()
        messages.success(request, "Task status updated successfully.")
    return redirect("list")


@login_required
def delete_task(request, task_id):
    """
    Delete a specific task for the logged-in user.

    This view handles deleting a specific task for the currently logged-in
    user. The task is deleted via a POST request.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the list view after deleting the
        task.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect("list")
    messages.error(request, "Failed to delete task.")
    return redirect("list")


def register(request):
    """
    Register a new user.

    This view handles the registration of a new user. The user details are
    provided via a POST request. If the registration is successful,
    the user is logged in and redirected to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page for registration.
        HttpResponseRedirect: Redirects to the home page after successful
        registration.
    """
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


@login_required
def profile(request):
    """
    Display and update the profile of the logged-in user.

    This view handles the display and update of the profile for the currently
    logged-in user. It also calculates various statistics about the user's
    tasks.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying and updating the
        profile.
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    tasks = Task.objects.filter(user=request.user)

    # Calculate statistics
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status="C").count()
    pending_tasks = tasks.filter(status="P").count()
    in_progress_tasks = tasks.filter(status="IP").count()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile,
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "in_progress_tasks": in_progress_tasks,
        "account_created": request.user.date_joined,
        "last_login": request.user.last_login,
    }

    return render(
        request,
        "tasks/profile.html",
        context,
    )
