from django.db import models

# Create your models here.

RL = 'RL'
TL = 'TL'
    
liner_choices = (
    (RL, 'Round Liner'),
    (TL, 'Tight Liner'),
)

class Round(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField(max_length=1)
    liner = models.CharField(max_length=32, choices=liner_choices, default=RL)
    stock = models.IntegerField(max_length=5)

    def __str__(self):
        return self.name
    