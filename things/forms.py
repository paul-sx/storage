from django.forms import ModelForm
from things.models import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']