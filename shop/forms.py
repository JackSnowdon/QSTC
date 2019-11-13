from django import forms

from .models import Round, RoundTube, Shader, Mag

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