from django.db import models
from django.contrib.auth.models import User

class Mountain(models.Model):
    name = models.CharField(max_length=20)
    approach = models.CharField(max_length=30)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    state = models.CharField(max_length=5,blank=True)
    country = models.CharField(max_length=20,blank=True)
    continent = models.CharField(max_length=20,blank=True)
    elevation = models.CharField(max_length=10,blank=True)
    google_maps_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class ClimbUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class ClimbEvent(models.Model):
    mountain = models.ForeignKey(Mountain, blank=True, null=True, on_delete=models.CASCADE)
    event_date = models.DateField(null=True)
    attendees = models.ManyToManyField(ClimbUser, blank=True) 
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='climb_events', null = True)
    completed = models.BooleanField(default=False)
    # party_size =
    # spots_available =
    # mountain = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.mountain)
        # summit_status = 'summited' if self.completed else 'posted'
        # return f'{self.mountain}: {summit_status}'


