from django import forms

from .models import Todo


class TodoCreateForm(forms.ModelForm):
    """
    Form for creating new todo
    """
    class Meta:
        model = Todo
        fields = [
            'message',
            'text_color',
            'background_color',
        ]
