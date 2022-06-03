from django.db import models

class Climb(models.Model):
    climb_date = models.DateField()
    mountain = models.CharField(max_length=50)

    def __str__(self):
        return self.mountain

    
