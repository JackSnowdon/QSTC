from django.urls import path
from .views import add_round, add_shader, delete_round, delete_shader, edit_round, edit_shader, shop

urlpatterns = [
    path('shop/', shop, name="shop"),
    path('add_round/', add_round, name="add_round"),
    path('add_shader/', add_shader, name="add_shader"),
    path(r'edit_round/<int:id>', edit_round, name="edit_round"),
    path(r'edit_shader/<int:id>', edit_shader, name="edit_shader"),
    path(r'delete_round/<int:pk>', delete_round, name="delete_round"),
    path(r'delete_shader/<int:pk>', delete_shader, name="delete_shader"),
]
