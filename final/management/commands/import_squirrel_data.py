from django.core.management import BaseCommand
from final.models import Location
import csv

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path',type = str)

    def handle(self,*args,**options):
        path = options['path']

        with open(path,'r') as fp:
            read = csv.DictReader(fp)
            for i in read:
               # print(i)
                Location.objects.create(
                        Latitude=i['X'],
                        Longtitude=i['Y'],
                        Unique_Squirrel_ID=i['Unique Squirrel ID'],
                        Shift=i['Shift'],
                        Date=i['Date'],
                        Age=i['Age'],
                        Primary_Fur = i['Primary Fur Color'],
                        Location = i['Location'],
                        Specific_Location = i['Specific Location'],
                        Running = True if i['Running']== 'TRUE' else False,
                        Chasing = True if i['Chasing']== 'TRUE' else False,
                        Climbing = True if i['Climbing']== 'TRUE' else False,
                        Eating = True if i['Eating']== 'TRUE' else False,
                        Foraging = True if i['Foraging']== 'TRUE' else False,
                        Other_Activities=i['Other Activities'],
                        Kuks = True if i['Kuks']== 'TRUE' else False,
                        Quaas=True if i['Quaas'] == 'TRUE' else False,
                        Moans=True if i['Moans'] == 'TRUE' else False,
                        Tail_Flags=True if i['Tail flags'] == 'TRUE' else False,
                        Tail_Twitches=True if i['Tail twitches'] == 'TRUE' else False,
                        Approaches=True if i['Approaches'] == 'TRUE' else False,
                        Indifferent=True if i['Indifferent'] == 'TRUE' else False,
                        Runs_From=True if i['Runs from'] == 'TRUE' else False,
                )
