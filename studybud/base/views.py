from django.http import HttpResponse
from django.shortcuts import render
from .models import Room


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Learn python!'},    
#     {'id': 2, 'name': 'Front-end Devs'},
#     {'id': 3, 'name': 'Version Control'},
# ]


# To create a view, use function based views in this case
def home(request):  # Request object is an http object
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)
