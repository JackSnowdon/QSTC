from django import forms

from .models import Round, Shader

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