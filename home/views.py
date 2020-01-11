from django.shortcuts import render
from .models import Artist

# Create your views here.

def index(request):
    return render(request, 'index.html')

def artists(request):
    tattoo_artists = Artist.objects.order_by("name")
    return render(request, 'artists.html', {"tattoo_artists": tattoo_artists})