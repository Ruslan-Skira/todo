"""
Module docstring
"""
from django.db import models


class Todo(models.Model):
    """
    Todo models
    """
    TEXT_COLOR_CHOICES = [
        ('red', 'red'),
        ('white', 'white'),
        ('green', 'green'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('yellow', 'yellow'),
    ]
    BACKGROUND_COLOR_CHOICES = [
        ('red', 'red'),
        ('white', 'white'),
        ('green', 'green'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('yellow', 'yellow'),
        ('black', 'black'),
    ]

    message = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    text_color = models.CharField(
        max_length=100,
        choices=TEXT_COLOR_CHOICES,
        default='black',
    )
    background_color = models.CharField(
        max_length=100,
        choices=BACKGROUND_COLOR_CHOICES,
        default='white',
    )
    class Meta:
        ordering = ['-data']
