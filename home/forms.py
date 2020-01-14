from django import forms

from .models import Artist

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        exclude = ['profile']

class EditArtist(forms.ModelForm):

    class Meta:
        model = Artist
        exclude = ['profile', 'image']