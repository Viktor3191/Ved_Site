from .models import Task  # импортируем из нашего приложения
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "decision"]
