from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Max, Q

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
    #form= LocationForm(request.POST or None)
    if request.method == 'POST':
        form= LocationForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            return JsonResponse({})

    form= LocationForm(instance=squirrel)
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


def stats(request):
    Total_Sightings = Location.objects.aggregate(total_sightings=Count('Unique_Squirrel_ID'))
    Age_Count = Location.objects.values('Age').annotate(age_count=Count('Age'))
    Shift_Count = Location.objects.values('Shift').annotate(shift_count=Count('Shift'))
    Latest_Sighting = Location.objects.aggregate(latest_sighting=Max('Date'))
    Fur_Color_Count = Location.objects.values('Primary_Fur').annotate(fur_color_count=Count('Primary_Fur'))
    context = {
            'Total_Sightings': Total_Sightings,
            'Age_Count': Age_Count,
            'Latest_Sighting': Latest_Sighting,
            'Fur_Color_Count': Fur_Color_Count,
            'Shift_Count': Shift_Count,
            }
    return render(request, 'sightings/stats.html', context)
