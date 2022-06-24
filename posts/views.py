from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import ClimbEvent
from .models import Mountain
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import MountainForm, ClimbEventForm, ClimbEventFormAdmin
from datetime import datetime
from django.conf import settings
import calendar
from calendar import HTMLCalendar
import requests

def search_events(request):
    if request.method == "POST":
        searched = request.POST['searched']
        events = ClimbEvent.objects.filter(event_date__contains=searched)
        return render(request,'posts/search_events.html',
            {'searched': searched, 'events': events})
    else:
        return render(request,'posts/search_events.html',
        { 'no_search': True })

def my_events(request):
    if request.user.is_authenticated:
        me = request.user.id
        events = request.user.attending_events.all()
        return render(request, 'posts/my_events.html',
        {'me':me, 'events':events})
    else:
        messages.success(request, ("You Do Not Have Permission To View This Page"))
        return redirect('climbs:list_events')

def delete_event(request,event_id):
    event = ClimbEvent.objects.get(pk=event_id)
    if request.user == event.user:
        event.delete()
        messages.success(request, ("Expedition Deleted"))
        return redirect('climbs:list_events')
    else:
        messages.success(request, ("Delete Permission Not Granted"))
        return redirect('climbs:list_events')

def update_event(request, event_id):
    event = ClimbEvent.objects.get(pk=event_id)
    form = ClimbEventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('climbs:list_events')
    return render(request,'posts/update_event.html',
        {'event': event,'form':form})

def add_event(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = ClimbEventFormAdmin(request.POST)
            if form.is_valid():
                event = form.save()
                event.attendees.add(event.user)
            return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = ClimbEventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.user = request.user # LOGGED IN USER
                event.save()
                event.attendees.add(request.user)
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        # JUST GOING TO THE PAGE, NOT SUBMITTING
        if request.user.is_superuser:
            form = ClimbEventFormAdmin
        else:
            form = ClimbEventForm
        
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'posts/add_event.html', {'form':form, 'submitted':submitted,})

def delete_mt(request,route_id):
    route = Mountain.objects.get(pk=route_id)
    route.delete()
    return redirect('climbs:list_routes')

def update_mt(request, route_id):
    route = Mountain.objects.get(pk=route_id)
    form = MountainForm(request.POST or None, instance=route)
    if form.is_valid():
        form.save()
        return redirect('climbs:list_routes')
    return render(request,'posts/update_mt.html',
        {'route': route,'form':form})

def search_mt(request):
    if request.method == "POST":
        searched = request.POST['searched']
        mountains = Mountain.objects.filter(name__contains=searched)
        return render(request,'posts/search_mt.html',
            {'searched': searched, 'mountains': mountains})
    else:
        return render(request,'posts/search_mt.html',
        { })
    
def show_mt(request, route_id):
    route = Mountain.objects.get(pk=route_id)
    # OPEN-WEATHER API #
    params = {
    'lat': route.latitude,
    'lon': route.longitude,
    'appid': settings.API_KEY,
    'exclude': 'minutely,hourly,daily,alerts',
    'units': 'imperial'
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=params)
    route_weather = response.json()
    # print(route_weather)
    return render(request,'posts/show_mt.html',
        {'route': route, 'route_weather':route_weather})

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
    route_list = Mountain.objects.all().order_by('name',)
    routes = []
    for letter in string.ascii_uppercase:
        letter_dict = {
            'letter': letter,
            'routes': route_list.filter(name__startswith=letter)
        }
        routes.append(letter_dict)
    return render(request, 'posts/route_list.html',
    {'route_list': route_list, 'routes':routes, })

def all_climbers(request):
    climber_list = User.objects.all().order_by('last_name',)
    return render(request, 'posts/climber_list.html',
    {'climber_list': climber_list})

def all_events(request):
    event_list = ClimbEvent.objects.all().order_by('event_date', )
    return render(request, 'posts/event_list.html',
        {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)
    now = datetime.now()
    current_year = now.year
    
    
    event_list = ClimbEvent.objects.filter(
        event_date__year = year,
        event_date__month = month_number )

    time = now.strftime('%I:%M %p')
    return render(request, 'posts/home.html', 
        {"year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time":time,
        "event_list": event_list,
        })

@login_required
def join_event(request, event_id):
    event = get_object_or_404(ClimbEvent, id=event_id)
    event.attendees.add(request.user)
    return redirect('climbs:list_events')
    
@login_required
def drop_event(request, event_id):
    event = get_object_or_404(ClimbEvent, id=event_id)
    event.attendees.remove(request.user)
    return redirect('climbs:list_events')
   
