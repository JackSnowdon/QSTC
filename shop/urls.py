from django.urls import path
from .views import add_round, add_shader, delete_round, edit_round, shop

urlpatterns = [
    path('shop/', shop, name="shop"),
    path('add_round/', add_round, name="add_round"),
    path('add_shader/', add_shader, name="add_shader"),
    path(r'edit_round/<int:id>', edit_round, name="edit_round"),
    path(r'delete_round/<int:pk>', delete_round, name="delete_round"),
]
