from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from .forms import TodoCreateForm
from .models import Todo


class TodoView(View):
    """
    Todo view
    """
    def get(self, request, *args, **kwargs):
        """
        GET method for function
        """
        form = TodoCreateForm()
        todos = Todo.objects.all()
        return render(request, "todo_task/todo_task.html", 
        context={'form': form, 'todos': todos})

    def post(self, request, *args, **kwargs):
        """
        Method save the todo message
        """
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            new_todo = form.save()
            return JsonResponse({'todo': 
            model_to_dict(new_todo)}, status=200)
        else:
            return redirect('todo')

class TodoDeleteView(View):
    """
    Todo delete view
    """
    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({'result': 'ok'}, status=200)
