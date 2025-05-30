from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Task


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


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def delete_model(self, request, obj):
        Task.objects.filter(user=obj).delete()
        super().delete_model(request, obj)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register the Profile model
admin.site.register(Profile)
