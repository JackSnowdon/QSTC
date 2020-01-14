from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Artist
from .forms import ArtistForm, EditArtist

# Create your views here.


def index(request):
    return render(request, "index.html")


def artists(request):
    tattoo_artists = Artist.objects.order_by("name")
    return render(request, "artists.html", {"tattoo_artists": tattoo_artists})


@login_required
def add_artist(request):
    if request.user.profile.staff_access:
        if request.method == "POST":
            artist_form = ArtistForm(request.POST, request.FILES or None)
            if artist_form.is_valid():
                artist = artist_form.save(commit=False)
                artist.profile = request.user.profile
                artist.save()
                messages.error(
                    request,
                    "Added {0}'s Artist Profile".format(artist.name),
                    extra_tags="alert",
                )
                return redirect("artists")
        else:
            artist_form = ArtistForm()
        return render(request, "add_artist.html", {"artist_form": artist_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("artists")


@login_required
def edit_artist(request, id):
    if request.user.profile.staff_access:   
        item = get_object_or_404(Artist, pk=id)
        if request.method == "POST":
            artist_form = EditArtist(request.POST, request.FILES or None, instance=item)
            if artist_form.is_valid():
                artist_form.save()
                messages.error(request, "Edited {0}".format(item.name), extra_tags="alert")
                return redirect("artists")
        else:
            artist_form = EditArtist(instance=item)
        return render(
            request, "edit_artist.html", {"artist_form": artist_form, "item": item}
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("artists")


@login_required
def delete_artist(request, id):
    if request.user.profile.staff_access:
        instance = Artist.objects.get(pk=id)
        messages.error(request, "Deleted {0}".format(instance), extra_tags="alert")
        instance.delete()
        return redirect(reverse("profile"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")