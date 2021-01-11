from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        #The user wants to sign up
        if request.POST['password1']== request.POST['password2']:
            try:
                user= User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username exists'})
            except User.DoesNotExist:
                user= User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        #The user wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user= auth.authenticate(username=request.POST['username'], password=request.POST['password'] )
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or Password incorrect'})
            
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')