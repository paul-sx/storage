
from django.urls import path
from things import views

urlpatterns = [
    path('', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>/', views.LocationDetailView.as_view(), name='location'),
    path('location/new/', views.LocationCreateView.as_view(), name='location_create'),
    path('location/<int:location_pk>/container/new/', views.ContainerCreateView.as_view(), name='container_create'),
    path('location/<int:location_pk>/container/<int:pk>/', views.ContainerDetailView.as_view(), name='container'),
    path('location/<int:location_pk>/container/<int:container_pk>/thing/<int:pk>/', views.ThingDetailView.as_view(), name='thing'),
]