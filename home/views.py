from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Artist
from .forms import ArtistForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def artists(request):
    tattoo_artists = Artist.objects.order_by("name")
    return render(request, 'artists.html', {"tattoo_artists": tattoo_artists})

@login_required
def add_artist(request):
    if request.user.profile.staff_access:
        if request.method == "POST":
            artist_form = ArtistForm(request.POST)
            if artist_form.is_valid():
                artist = artist_form.save(commit=False)
                artist.profile = request.user.profile
                artist.save()
                return redirect("artists")
        else:
            artist_form = ArtistForm()
        return render(request, "add_artist.html", {"artist_form": artist_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")