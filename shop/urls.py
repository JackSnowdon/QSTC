from django.urls import path
from .views import add_round, shop

urlpatterns = [
    path('shop/', shop, name="shop"),
    path('add_round/', add_round, name="add_round"),
]