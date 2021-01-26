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