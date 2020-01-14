from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('artist/', artists, name="artists"),
    path("add_artist/", add_artist, name="add_artist"),
    path(r"edit_artist/<int:id>", edit_artist, name="edit_artist"),
    path(r"delete_artist/<int:id>", delete_artist, name="delete_artist"),
]