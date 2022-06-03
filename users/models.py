from django.db import models

class Climber(models.Model):
    first_name = models.CharField (max_length=50)
    last_name = models.CharField (max_length=50)

    def __str__(self):
        return self.last_name, self.first_name
