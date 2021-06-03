from django.shortcuts import get_object_or_404, render
from things.models import Location, Container, Thing
from django.views.generic import ListView, DetailView, UpdateView
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

class LocationCreateView(CreateView):
    model = Location
    fields = ['name',]
    template_name = 'things/location_create.html'

class LocationUpdateView(UpdateView):
    model = Location
    fields = ['name',]
    template_name = 'things/location_edit.html'

class ContainerDetailView(DetailView):
    model = Container
    template_name = 'things/container_detail.html'
    context_object_name = 'container'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['things'] = Thing.objects.filter(container=self.get_object())
        context['location'] = get_object_or_404(Location, pk=self.kwargs.get('location_pk'))
        return context
        

class ContainerUpdateView(UpdateView):
    model = Container
    fields = ['name', 'location']
    context_object_name = 'container'
    template_name = 'things/container_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = get_object_or_404(Location, pk=self.kwargs.get('location_pk'))
        return context


class ContainerCreateView(CreateView):
    model = Container
    fields = ['name', 'location']
    template_name = 'things/container_create.html'

    def get_initial(self):
        location = get_object_or_404(Location,  pk=self.kwargs.get('location_pk'))
        return {
            'location': location
        }


class ThingDetailView(DetailView):
    model = Thing
    template_name = 'things/thing_detail.html'
    context_object_name = 'thing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['container'] = get_object_or_404(Container, pk=self.kwargs.get('container_pk'))
        context['location'] = get_object_or_404(Location, pk=self.kwargs.get('location_pk'))
        return context


class ThingCreateView(CreateView):
    model = Thing
    fields = ['name', 'description', 'container']
    template_name = 'things/thing_create.html'

    def get_initial(self):
        container = get_object_or_404(Container, pk=self.kwargs.get('container_pk'))
        return {
            'container': container
        }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['container'] = get_object_or_404(Container, pk=self.kwargs.get('container_pk'))
        context['location'] = get_object_or_404(Location, pk=self.kwargs.get('location_pk'))
        return context


class ThingUpdateView(UpdateView):
    model = Thing
    fields = ['name', 'description', 'container']
    template_name = 'things/thing_edit.html'
    context_object_name = 'thing'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['container'] = get_object_or_404(Container, pk=self.kwargs.get('container_pk'))
        context['location'] = get_object_or_404(Location, pk=self.kwargs.get('location_pk'))
        return context
