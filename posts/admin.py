from django.contrib import admin

from .models import Mountain, ClimbUser, ClimbEvent

admin.site.register(Mountain)
admin.site.register(ClimbUser)
admin.site.register(ClimbEvent)

