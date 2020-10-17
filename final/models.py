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
    Running = models.NullBooleanField()
    Chasing = models.NullBooleanField()
    Climbing = models.NullBooleanField()
    Eating = models.NullBooleanField()
    Foraging = models.NullBooleanField()

    Other_Activities = models.CharField(max_length=100, blank=True)
    Kuks = models.NullBooleanField()
    Quaas = models.NullBooleanField()
    Moans = models.NullBooleanField()
    Tail_Flags = models.NullBooleanField()
    Tail_Twitches = models.NullBooleanField()
    Approaches = models.NullBooleanField()
    Indifferent = models.NullBooleanField()
    Runs_From = models.NullBooleanField()

    def __str__(self):
        return self.Unique_Squirrel_ID

