from django.db import models

class Location(models.Model):
    Latitude = models.FloatField()
    Longtitude = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length = 100)
    
    AM = 'AM'
    PM = 'PM'
    OTHER = ''
    shift_choice = [
            (AM, 'AM'),
            (PM, 'PM'),
            (OTHER, '')
            ]
    Shift = models.CharField(
            max_length = 15,
            choices = shift_choice,
            default = OTHER,
            )
    
    Date = models.CharField(max_length = 100,default = '')
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    age_choice = [
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (OTHER,''),
            ]
    Age = models.CharField(
        max_length=30,
        choices=age_choice,
        default=OTHER,
        blank=True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    fur_choice = [
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (OTHER, ''),
    ]

    Primary_Fur = models.CharField(
        max_length=30,
        choices=fur_choice,
        default=OTHER,
        blank=True,
    )

    GROUND = 'Ground'
    ABOVE = 'Above'
    location_choice = [
        (GROUND, 'Ground'),
        (ABOVE, 'Above'),
        (OTHER, ''),
    ]

    Location = models.CharField(
        max_length=30,
        choices=location_choice,
        default=OTHER,
        blank=True,
    )

    Specific_Location = models.CharField(max_length=100, blank=True)
    Running = models.BooleanField(null = True)
    Chasing = models.BooleanField(null = True)
    Climbing = models.BooleanField(null = True)
    Eating = models.BooleanField(null = True)
    Foraging = models.BooleanField(null = True)

    Other_Activities = models.CharField(max_length=100, blank=True)
    Kuks = models.BooleanField(null = True)
    Quaas = models.BooleanField(null = True)
    Moans = models.BooleanField(null = True)
    Tail_Flags = models.BooleanField(null = True)
    Tail_Twitches = models.BooleanField(null = True)
    Approaches = models.BooleanField(null = True)
    Indifferent = models.BooleanField(null = True)
    Runs_From = models.BooleanField(null = True)

    
    def __str__(self):
        return self.Unique_Squirrel_ID

