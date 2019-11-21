from django.db import models
import datetime
from django.utils import timezone

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


class RoundTube(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    liner = models.CharField(max_length=32, default="Round Tube")
    ton = models.CharField(max_length=20, choices=NT_CHOICES, default=Tubes)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Vtip(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    liner = models.CharField(max_length=32, default="V Tube")
    ton = models.CharField(max_length=20, choices=NT_CHOICES, default=Tubes)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Flat(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    liner = models.CharField(max_length=32, default="Flat Tube")
    ton = models.CharField(max_length=20, choices=NT_CHOICES, default=Tubes)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class StockObject(models.Model):
    name = models.CharField(max_length=50)
    stock = models.IntegerField()

    def __str__(self):
        return '{0} x {1}'.format(self.name, self.stock)


class StockReport(models.Model):
    date = models.DateTimeField(auto_now=True)
    stockitems = models.ManyToManyField(StockObject)
    

    def __str__(self):  
        return 'Stock Report {0} Completed on {1}'.format(self.id, self.date.date())