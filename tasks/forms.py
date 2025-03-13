from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["user", "created", "completed_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(
                attrs={
                    "cols": 25,
                    "placeholder": "Enter task description here",
                }
            ),
        }
