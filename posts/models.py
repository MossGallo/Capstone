from django.db import models
from django.contrib.auth.models import User

class ClimbEvent(models.Model):
    mountain = models.CharField(max_length=50)
    climb_date = models.DateField(null=True)
    completed = models.BooleanField('summited', default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='climb_events', null = True)
    
    def __str__(self):
        summit_status = 'summited' if self.completed else 'posted'
        return f'{self.mountain}: {summit_status}'    
