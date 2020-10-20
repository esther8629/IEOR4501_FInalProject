from django.forms import ModelForm

from final.models import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = [
                'Latitude',
                'Longtitude',
                'Unique_Squirrel_ID',
                'Shift',
                'Date',
                'Age',
                ]

class AddForm(ModelForm):
    class Meta:
        model = Location
        fields = [
                'Latitude',
                'Longtitude',
                'Unique_Squirrel_ID',
                'Shift',
                'Date',
                'Age',
                ]
