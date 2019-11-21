from django import forms

from .models import Flat, Round, RoundTube, Shader, StockReport, StockObject, Mag, Vtip

class RoundForm(forms.ModelForm):

    class Meta:
        model = Round
        exclude = ['name', 'ton']

class EditRoundForm(forms.ModelForm):

    class Meta:
        model = Round
        exclude = ['name', 'liner', 'size', 'ton']

class ShaderForm(forms.ModelForm):

    class Meta:
        model = Shader
        exclude = ['name', 'liner', 'ton']

class EditShaderForm(forms.ModelForm):

    class Meta:
        model = Shader
        exclude = ['name', 'liner', 'size', 'ton']

class MagForm(forms.ModelForm):

    class Meta:
        model = Mag
        exclude = ['name', 'liner', 'ton']


class EditMagForm(forms.ModelForm):

    class Meta:
        model = Mag
        exclude = ['name', 'liner', 'size', 'ton']

class RoundTubeForm(forms.ModelForm):

    class Meta:
        model = RoundTube
        exclude = ['name', 'liner', 'ton']


class EditRoundTubeForm(forms.ModelForm):

    class Meta:
        model = RoundTube
        exclude = ['name', 'liner', 'size', 'ton']

class VtipForm(forms.ModelForm):

    class Meta:
        model = Vtip
        exclude = ['name', 'liner', 'ton']


class EditVtipForm(forms.ModelForm):

    class Meta:
        model = Vtip
        exclude = ['name', 'liner', 'size', 'ton']

class FlatForm(forms.ModelForm):

    class Meta:
        model = Flat
        exclude = ['name', 'liner', 'ton']


class EditFlatForm(forms.ModelForm):

    class Meta:
        model = Flat
        exclude = ['name', 'liner', 'size', 'ton']

class StockForm(forms.ModelForm):

    class Meta:
        model = StockReport
        fields = '__all__'

class StockObjectForm(forms.ModelForm):

    class Meta:
        model = StockObject
        fields = '__all__'