from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Todo


def todo(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todos/todo.html', context)


def todo_insert(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('list/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/list/')

