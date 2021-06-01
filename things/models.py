from django.db import models
from django.urls import reverse

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255, default='', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location", kwargs={"pk": self.pk})
    

class Container(models.Model):
    name = models.CharField(max_length=255, default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', 'pk']

    def __str__(self):
        return f'{self.name} - {self.pk}'

    def get_absolute_url(self):
        return reverse("container", kwargs={"pk": self.pk, "location_pk": self.location.pk})
    


class Thing(models.Model):
    name = models.CharField(max_length=255, default='')
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    description = models.TextField(default='')
    

    class Meta:
        ordering = ['name', 'pk']

    def __str__(self):
        return f'{self.name} - {self.pk}'

    def get_absolute_url(self):
        return reverse("thing", kwargs={"pk": self.pk, "container_pk": self.container.pk, "location_pk": self.container.location.pk})
