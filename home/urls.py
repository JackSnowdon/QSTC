from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('artist/', artists, name="artists"),
    path("add_artist/", add_artist, name="add_artist"),
]