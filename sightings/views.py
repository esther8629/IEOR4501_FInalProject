from django.shortcuts import render
from django.http import JsonResponse

from final.models import Location
from sightings.forms import LocationForm
from sightings.forms import AddForm

def show(request):
    locations = Location.objects.all()
    context = {
            'locations':locations
            }
    return render(request,'sightings/show.html',context)

def detail(request,Unique_Squirrel_ID):
    squirrel = Location.objects.get(Unique_Squirrel_ID = Unique_Squirrel_ID)
    form= LocationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({})

    context = {
           'form':form
            }
    return render(request, 'sightings/detail.html',context)


def add_sightings(request):
    addform = AddForm(request.POST)
    if request.method == 'POST':
        if addform.is_valid():
            addform.save()
            return JsonResponse({})
        else:
            return JsonResponse({'Errors':addform.errors}, status=400)
    
    context = {
            'addform': addform
            }
    return render(request, 'sightings/add_sightings.html',context)
