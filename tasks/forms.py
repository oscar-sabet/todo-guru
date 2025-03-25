from .models import Task, Profile
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "due_date",
            "priority",
            "category",
            "status"
            ]
        exclude = ["user", "created", "completed_date"]  # , "status"]
        widgets = {
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "description": forms.Textarea(
                attrs={
                    "cols": 25,
                    "placeholder": "Enter task description here",
                    # "status": forms.HiddenInput(attrs={"value": "P"}),
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 60:
            raise forms.ValidationError(
                "The title must be 60 characters or less."
                )
        return title


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"})
                               )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture"]
