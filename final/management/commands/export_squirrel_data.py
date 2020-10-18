from django.core.management import BaseCommand
from final.models import Location
import csv

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path',type = str)

    def handle(self,*args,**options):
        path = options['path']
        fields = [f.name for f in Location._meta.fields[1:]]
        
        with open(path,'w',newline='') as csvfile:
            writer = csv.writer(csvfile,quoting=csv.QUOTE_ALL, delimiter=',')
            writer.writerow(fields)
            
            for l in Location.objects.all():
                instance = [getattr(l,f) for f in fields]
                writer.writerow(instance)
