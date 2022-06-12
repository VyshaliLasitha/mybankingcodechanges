from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login/')





def loginpage(request):
    if request.method == "POST" and 'form1' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(5000)
            return redirect('/')
        else:
            messages.error(request, 'INCORRECT USERNAME OR PASSWORD! TRY AGAIN')

    form = CreateUserForm()
    if request.method == 'POST' and 'form2' in request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created Successfully for ' + username)

    context = {'form': form }

    return render(request, 'login.html', context)

# @login_required(login_url='/login/')
def index(request):
    context= {}
    return render (request, 'home.html' , context)