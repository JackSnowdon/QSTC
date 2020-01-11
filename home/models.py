from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist')
    about = models.TextField()
    twitter_handle = models.CharField(max_length=30, blank=True)
    instagram_handle = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.name