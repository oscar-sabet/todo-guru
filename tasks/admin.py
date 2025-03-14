from django.contrib import admin

# Register your models here.
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "category",
        "user",
        "created",
        "due_date",
        "completed_date",
    )
    list_filter = ("status", "priority", "category", "user")
    search_fields = ("title", "description")
