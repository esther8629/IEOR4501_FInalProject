from django.shortcuts import render
from final.models import Location
from sightings.forms import LocationForm

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

