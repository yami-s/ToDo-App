from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks=ToDo.objects.all()
    form=ToDoForm()
    
    if request.method=='POST':
        form=ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    
    context={'tasks':tasks,'form':form}
    return render(request,'tasks/index.html',context)
    
def updateTask(request,pk):
    task=ToDo.objects.get(id=pk)
    form=ToDoForm(instance=task)
    
    if request.method=='POST':
        form=ToDoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context={'form':form}
    return render(request,'tasks/update_task.html',context)     

def deleteTask(request,pk):
    task=ToDo.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    
    context={'task':task}
    return render(request,'tasks/delete.html',context)  