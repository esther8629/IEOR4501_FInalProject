from django.urls import path

from . import views
app_name = 'sightings'

urlpatterns = [
        path('',views.show,name ='show'),
        path('add/',views.add_sightings,name = 'add'),
        path('stats/', views.stats,name = 'stats'),
        path('<Unique_Squirrel_ID>/',views.detail,name = 'detail'),
        ]
