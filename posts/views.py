from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import ClimbEvent
from .models import Mountain
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import MountainForm
import calendar
from calendar import HTMLCalendar

def show_mt(request, route_id):
    route = Mountain.objects.get(pk=route_id)
    return render(request,'posts/show_mt.html',
        {'route': route})

def add_mt(request):
    submitted = False
    if request.method == "POST":
        form = MountainForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_mt?submitted=True')
    else:
        form = MountainForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'posts/add_mt.html', {'form':form, 'submitted':submitted, })

def all_routes(request):
    import string
    route_list = Mountain.objects.all()
    routes = []
    for letter in string.ascii_uppercase:
        letter_dict = {
            'letter': letter,
            'routes': route_list.filter(name__startswith=letter)
        }
        routes.append(letter_dict)
    for route in routes:
        print(route)
        print()
    return render(request, 'posts/route_list.html',
    {'route_list': route_list, 'routes':routes, })

def all_climbers(request):
    climber_list = User.objects.all()
    return render(request, 'posts/climber_list.html',
    {'climber_list': climber_list})

def all_events(request):
    event_list = ClimbEvent.objects.all()
    return render(request, 'posts/event_list.html',
        {'event_list': event_list})

def index(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('users:login')
        print(request.POST)
        mountain = request.POST.get('mountain')
        event_date = request.POST.get('event_date')
        
        ClimbEvent.objects.create(
            mountain_id = mountain,
            event_date = event_date,
            user=request.user
        )
        return redirect('climbs:home')
    context = {}
    
    if request.user.is_authenticated:
        climbs = request.user.climb_events.all()
        mountains = Mountain.objects.all()
        context = {
            'climbs_complete': climbs.filter(completed=True),
            'climbs_incomplete': climbs.filter(completed=False),
            'mountains': mountains
        }
    return render(request, 'posts/index.html', context)

@login_required
def toggle_complete(request, id):
    climb = get_object_or_404(ClimbEvent, id = id)

    if climb.user != request.user:
        return redirect('climbs:home')
    
    climb.completed = not climb.completed
    climb.save()
    return redirect('climbs:home')

@login_required
def delete(request,id):
    climb = get_object_or_404(ClimbEvent, id=id)

    if climb.user != request.user:
        return redirect('climbs:home')
    climb.delete()
    return redirect('climbs:home')

@login_required
def join(request, id):
    return redirect('clims:list_events')
    pass

@login_required
def drop(request, id):
    return redirect('clims:list_events')
    pass
