from django.contrib import admin
from things.models import Location, Container, Thing

# Register your models here.

admin.site.register(Location)
admin.site.register(Container)
admin.site.register(Thing)
