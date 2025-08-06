from rest_framework import viewsets
from .models import Place
from .serializers import PlaceSerializer
from django.shortcuts import render
from django.conf import settings

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

def map_view(request):
    return render(request, "mapplaces/map.html", {"geoapify_key": settings.GEOAPIFY_KEY})
