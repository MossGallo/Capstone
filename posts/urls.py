from django.urls import path
from .import views

app_name = 'climbs'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('events', views.all_events, name='list_events'),
    path('climbers', views.all_climbers, name='list_climbers'),
    path('routes', views.all_routes, name='list_routes'),
    path('add_mt', views.add_mt, name='add-mt'),
    path('add_event', views.add_event, name='add-event'),
    path('my_events', views.my_events, name='my-events'),
    path('search_mt', views.search_mt, name='search-mt'),
    path('update_mt/<route_id>', views.update_mt, name='update-mt'),
    path('update_event/<event_id>', views.update_event, name='update-event'),
    path('show_mt/<route_id>', views.show_mt, name='show-mt'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('delete_mt/<route_id>', views.delete_mt, name='delete-mt'),
    path('toggle-complete/<int:id>/', views.toggle_complete, name ='toggle_complete'),
    path('delete/<int:id>/', views.delete, name = 'delete'),
]

