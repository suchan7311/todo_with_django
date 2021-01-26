from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
    todos=Todo.objects.all()
    content={'todos':todos}
    return render(request, 'todolist_app/index.html',content)

def createTodo(request):
    todoContent=request.POST['todoContent']
    new_todo=Todo(content=todoContent)
    new_todo.save()
    return HttpResponseRedirect(reverse("index"))

def deleteTodo(request):
    delete_todo_id= request.GET['todoNum']
    print("완료 todo id",delete_todo_id)
    todo=Todo.objects.get(id=delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse("index"))