from django import forms

from .models import Round

class RoundForm(forms.ModelForm):

    class Meta:
        model = Round
        exclude = ['name']

class EditRoundForm(forms.ModelForm):

    class Meta:
        model = Round
        exclude = ['name', 'liner', 'size']