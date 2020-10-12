from django.shortcuts import render
from .models import Location
import random

def index(request):
    locations = Location.objects.all()
    locations_random = Location.objects.order_by('?')[:80]
    context = {
            'locations':locations_random,
            }

    return render(request,'final/index.html',context)

