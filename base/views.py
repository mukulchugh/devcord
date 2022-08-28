from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from .models import Room, Topic
from .forms import RoomForm



def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User not found.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username or Password is incorrect')
    context = { 'page': page }
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):
    page = 'register'
    if request.user.is_authenticated:
        return redirect('home')
    form = UserCreationForm()

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     password2 = request.POST.get('password2')

    #     if password == password2:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request, 'Username already exists')
    #             return redirect('register')
    #         else:
    #             user = User.objects.create_user(username=username, password=password)
    #             user.save()
    #             messages.success(request, 'User created')
    #             return redirect('login')
    #     else:
    #         messages.info(request, 'Passwords do not match')
    #         return redirect('register')
    context = { 'page': page, 'form': form }
    return render(request, 'base/login_register.html', context)    

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    topic = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topic': topic, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'base/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('You are not allowed to edit this room.')
    else :
        if request.method == 'POST':
            form = RoomForm(request.POST, instance=room)
            if form.is_valid():
                form.save()
                return redirect('home')
        context={'form':form}
        return render(request, 'base/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context={'obj':room}
    return render(request, 'base/delete.html',context)