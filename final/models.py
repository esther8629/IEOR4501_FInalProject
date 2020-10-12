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
    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()

    Other_Activities = models.CharField(max_length=100, blank=True)
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_Flags = models.BooleanField()
    Tail_Twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_From = models.BooleanField()

    def __str__(self):
        return self.Unique_Squirrel_ID

