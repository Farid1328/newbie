from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . forms import Userform, Profileform
from . models import Profile


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    page = 'register'
    form = Userform()
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'page' : page}
    return render(request, 'users/login_register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('no user')
    context = {'page' : page}
    return render(request, 'users/login_register.html', context)

def logoutpage(request):
    logout(request)
    return redirect('index')


def profile(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(id=pk)
    '''if request.user == profile.owner:
        print(request.user)
    else:
        return redirect('index')
        print('not owner')'''
    context = {'user': user}
    return render(request, 'users/profile.html', context)

def profileform(request, pk):
    profile = Profile.objects.get(id=pk)
    form = Profileform(instance=profile)
    if request.user == profile.owner:
        print(request.user)
    else:
        return redirect('index')
        print('This is not yours')
    if request.method == 'POST':
        form = Profileform(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            print(profile.owner)
            profile.save()
            return redirect('index')
    context = {'form' : form}
    return render(request, 'users/user-form.html', context)