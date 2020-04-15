from django.urls import path

from .views import *

urlpatterns = [
    path('', TodoView.as_view(), name='todo'),
    path('<str:id>/delete/', TodoDeleteView.as_view(), name='todo_delete_url'),
]