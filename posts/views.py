from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import ClimbEvent

def all_events(request):
    event_list = ClimbEvent.objects.all()
    return render(request, 'posts/event_list.html',
        {'event_list': event_list})


def index(request):
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('users:login')
        mountain = request.POST.get('mountain')
        event_date = request.POST.get('event_date')
        ClimbEvent.objects.create(
            mountain = mountain,
            event_date = event_date,
            user=request.user
        )
        return redirect('climbs:home')
    context = {}
    
    if request.user.is_authenticated:
        climbs = request.user.climb_events.all()
        context = {
            'climbs_complete': climbs.filter(completed=True),
            'climbs_incomplete': climbs.filter(completed=False),
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