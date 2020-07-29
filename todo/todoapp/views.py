from django.shortcuts import render, redirect
from todoapp.forms import Newtask
from todoapp.models import Todo
# Create your views here.
def newtask(request):
    form = Newtask()
    if request.method == 'POST':
        form = Newtask(request.POST)
        if form.is_valid():
            nm = form.cleaned_data.get('title')
            dn = form.cleaned_data.get('description')
            dt = form.cleaned_data.get('date')
            reg = Todo(title = nm, description = dn, date = dt)
            reg.save()
            form = Newtask()
            return redirect('home')
    else:
        form = Newtask()
        tasks = Todo.objects.all()

    return render(request, 'todoapp/home.html', {'form':form, 'tasks':tasks})

def updatetask(request, id):
    if request.method == 'POST':
        pi = Todo.objects.get(pk = id)
        form = Newtask(request.POST, instance = pi)
        if form.is_valid():
            form.save()
    else:
        pi = Todo.objects.get(pk = id)
        form = Newtask(instance = pi)
    return render(request, 'todoapp/update.html', {'form':form})


def deletetask(request, id):
    if request.method == 'POST':
        dt = Todo.objects.get(pk = id)
        dt.delete()
        return redirect('home')
