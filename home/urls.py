from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('artist/', artists, name="artists"),
]