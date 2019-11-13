from django.db import models

# Create your models here.

RL = 'RL'
TL = 'TL'
Needles = 'Neeedles'
Tubes = 'Tubes'

liner_choices = (
    (RL, 'Round Liner'),
    (TL, 'Tight Liner'),
)

NT_CHOICES = (
    (Needles, 'Needles'),
    (Tubes, 'Tubes'),
)

class Round(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    liner = models.CharField(max_length=32, choices=liner_choices, default=RL)
    ton = models.CharField(max_length=20, choices=NT_CHOICES, default=Needles)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    

class Shader(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    liner = models.CharField(max_length=32, default="Round Shader")
    ton = models.CharField(max_length=20, choices=NT_CHOICES, default=Needles)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Mag(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    liner = models.CharField(max_length=32, default="Magnum Shader")
    ton = models.CharField(max_length=20, choices=NT_CHOICES, default=Needles)
    stock = models.IntegerField()

    def __str__(self):
        return self.name