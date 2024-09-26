from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from task_manager.models import Worker, Task


class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
            "team",
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = (
            "first_name",
            "last_name",
            "email",
            "position",
            "team",
        )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "search by username"
        })
    )


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "search by name of project"
        })
    )


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "priority",
            "deadline",
            "is_completed",
            "task_type",
            "project",
            "assignees",
        ]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        today = datetime.now().date()

        if deadline < today:
            raise ValidationError(
                "The deadline must be a date in the future."
            )

        return deadline


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "search by name of task"
        })
    )
