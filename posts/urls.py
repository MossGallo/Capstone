from django.urls import path

from .import views

app_name = "climbs"
urlpatterns = [
    path('', views.index, name = 'home'),
    path('events', views.all_events, name='list_events'),
    path('climbers', views.all_climbers, name='list_climbers'),
    path('routes', views.all_routes, name='list_routes'),
    path('toggle-complete/<int:id>/', views.toggle_complete, name ='toggle_complete'),
    path('delete/<int:id>/', views.delete, name = 'delete'),
]

