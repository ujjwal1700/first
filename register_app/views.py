from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views
from register_app.decorators import login_excluded

# Create your views here.

@login_excluded('home')
def register(request):
      f=RegisterForm()
      if request.method=='POST':
          f=RegisterForm(request.POST)
          if f.is_valid():
            f.save()
            messages.success(request,'User is Registered!')
            return redirect('login')


      context={'form':f}
      return render(request,'register_app/register.html',context)
