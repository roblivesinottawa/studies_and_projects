from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoview(req):
    all_to_items = TodoItem.objects.all()
    return render(req, 'todo.html',
        {'all_items': all_to_items})


def addTodo(req):
    new_item = TodoItem(content = req.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(req, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

    
