from django.urls import path

from . import views
app_name = 'final'

app_name = 'final'

urlpatterns = [
    path('',views.index,name = 'index')
        ]
