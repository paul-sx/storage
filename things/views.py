from django.shortcuts import get_object_or_404, render
from things.models import Location, Container, Thing
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from things.forms import LocationForm

# Create your views here.

class LocationListView(ListView):
    model = Location
    context_object_name = 'locations'
    template_name = "things/location_list.html"


class LocationDetailView(DetailView):
    model = Location
    template_name = 'things/location_detail.html'
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['containers'] = Container.objects.filter(location=self.get_object())
        return context


class ContainerDetailView(DetailView):
    model = Container
    template_name = 'things/container_detail.html'
    context_object_name = 'container'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['things'] = Thing.objects.filter(container=self.get_object())
        return context

class LocationCreateView(CreateView):
    model = Location
    fields = ['name',]
    template_name = 'things/location_create.html'


class ContainerCreateView(CreateView):
    model = Container
    fields = ['name', 'location']
    template_name = 'things/container_create.html'

    def get_initial(self):
        location = get_object_or_404(Location,  pk=self.kwargs.get('location_pk'))
        return {
            'location': location
        }
