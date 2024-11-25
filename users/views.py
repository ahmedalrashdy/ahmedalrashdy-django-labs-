from django.shortcuts import render, redirect,reverse,get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            # useremail = User.objects.get(email=email)

            if User.objects.filter(email=email):
                return render(request,'user_register.html',{'form':form,'exist':'the email is aready exist'})
            
            form.save()

            user = form.cleaned_data.get('username')


            messages.success(request,f"User {user} created successfully")

            return redirect('user:login')

        else:

            return render(request,'user_register.html',{'form':form})
    else:
        form = RegisterForm()

        return render(request,'user_register.html',{'form':form})
        

def userlogin(request):
    if request.user.is_authenticated:
        return redirect("patients:home")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        username = User.objects.get(email=email).username
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('patients:home')
        else:
            messages.error(request,'Invalid username or password')

            return redirect('user:login')
    return render(request,'user_login.html')
def userlogout(request):
    logout(request)
    return redirect('user:login')