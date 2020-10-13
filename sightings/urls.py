from django.urls import path

from . import views
app_name = 'sightings'

urlpatterns = [
        path('',views.show),
        path('<str:Unique_Squirrel_ID>/',views.detail,name = 'detail')
        ]
