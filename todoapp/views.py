from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):

   return render(request,'todoapp/home.html')





@login_required(login_url='login')
def index(request):
    f=TaskForm()
    if request.method =='POST':
        f=TaskForm(request.POST)
        if f.is_valid():
            f.save(commit=False).logger = request.user
            f.save()
            messages.success(request,"Task added successfully")
        return redirect('index')

    else:

            t= Task.objects.filter(logger=request.user)
            paginator=Paginator(t,5)
            page_number = request.GET.get('page')
            t = paginator.get_page(page_number)
            context={'tasks':t}
            return render(request,'todoapp/index.html',context)

@login_required(login_url='login')
def contact(request):
    context={'welcome':"Welcome to contact page"}
    return render(request,'todoapp/contact.html',context)

@login_required(login_url='login')
def about(request):
    context={'welcome': "Welcome to about page"}
    return render(request,'todoapp/about.html',context)

@login_required(login_url='login')
def delete(request,id):
    t=Task.objects.get(pk=id)
    if t.logger== request.user:
        t.delete()
        return redirect('index')
    else:
        messages.error(request,("You are not authorised to do this!"))
        return redirect('index')


@login_required(login_url='login')
def status(request,id):
     t=Task.objects.get(pk=id)
     if t.logger== request.user:
         if  t.completed :
             t.completed=False
             t.save()
             messages.warning(request,("Task changed to pending"))
         else:
             t.completed=True
             t.save()
             messages.success(request,("Task changed to completed"))

     else:
        messages.error(request,("You are not authorised to do this!"))
     return redirect('index')






@login_required(login_url='login')
def update(request,id):
    t=Task.objects.get(pk=id)
    if request.method=='POST':
        form = TaskForm(request.POST,instance=t)
        if form.is_valid():
            form.save()
            messages.success(request,("Task edited"))

        return redirect('index')

    else:

        context={'task':t}
        return render(request,'todoapp/update.html',context)
