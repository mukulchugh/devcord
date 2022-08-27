from django.shortcuts import render

rooms = [
    {'id': 1,'name': 'Lets learn Python'},
    {'id': 2,'name': 'djflk'},
    {'id': 3,'name': 'heyy'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    return render(request, 'base/room.html')