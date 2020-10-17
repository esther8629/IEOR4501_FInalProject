from django.urls import path

from . import views
app_name = 'sightings'

urlpatterns = [
        path('sightings/',views.show),
        path('add/',views.add_sightings, name = 'add'),
        path('<Unique_Squirrel_ID>/',views.detail,name = 'detail'),
        ]
