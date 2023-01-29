from dataclasses import fields
from .models import Task  # импортируем из нашего приложения
from django.forms import ModelForm, TextInput, Textarea, widgets


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "decision"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'введите название'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'введите описание'}),
                   "decision": Textarea(attrs={'class': 'form-control', 'placeholder': 'введите решение'})
                   }
