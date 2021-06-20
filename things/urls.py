
from django.urls import path, include
from things import views

urlpatterns = [
    path('', views.LocationListView.as_view(), name='locations'),
    path('search/', include('haystack.urls')),
    path('location/<int:pk>/', views.LocationDetailView.as_view(), name='location'),
    path('location/new/', views.LocationCreateView.as_view(), name='location_create'),
    path('location/<int:pk>/edit/', views.LocationUpdateView.as_view(), name='location_edit'),
    path('location/<int:location_pk>/container/new/', views.ContainerCreateView.as_view(), name='container_create'),
    path('location/<int:location_pk>/container/<int:pk>/', views.ContainerDetailView.as_view(), name='container'),
    path('location/<int:location_pk>/container/<int:container_pk>/thing/<int:pk>/', views.ThingDetailView.as_view(), name='thing'),
    path('location/<int:location_pk>/container/<int:pk>/edit/', views.ContainerUpdateView.as_view(), name='container_edit'),
    path('location/<int:location_pk>/container/<int:container_pk>/thing/new/', views.ThingCreateView.as_view(), name='thing_create'),
    path('location/<int:location_pk>/container/<int:container_pk>/thing/<int:pk>/edit/', views.ThingUpdateView.as_view(), name='thing_edit'),
]