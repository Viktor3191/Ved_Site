from dataclasses import fields
from .models import Task  # импортируем из нашего приложения
from django.forms import ModelForm, widgets, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "decision"]
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'введите название'}),
                   'task': TextInput(attrs={'class': 'form-control', 'placeholder': 'введите описание'}),
                   'decision': TextInput(attrs={'class': 'form-control', 'placeholder': 'введите решение'})
                   }
