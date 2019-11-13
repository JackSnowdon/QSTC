from django.urls import path
from .views import (
    add_round,
    add_round_tube,
    add_shader,
    add_mag,
    delete_round,
    delete_round_tube,
    delete_shader,
    delete_mag,
    edit_round,
    edit_round_tube,
    edit_shader,
    edit_mag,
    shop,
)

urlpatterns = [
    path("shop/", shop, name="shop"),
    path("add_round/", add_round, name="add_round"),
    path("add_shader/", add_shader, name="add_shader"),
    path("add_mag/", add_mag, name="add_mag"),
    path("add_round_tube/", add_round_tube, name="add_round_tube"),
    path(r"edit_round/<int:id>", edit_round, name="edit_round"),
    path(r"edit_shader/<int:id>", edit_shader, name="edit_shader"),
    path(r"edit_mag/<int:id>", edit_mag, name="edit_mag"),
    path(r"edit_round_tube/<int:id>", edit_round_tube, name="edit_round_tube"),
    path(r"delete_round/<int:pk>", delete_round, name="delete_round"),
    path(r"delete_shader/<int:pk>", delete_shader, name="delete_shader"),
    path(r"delete_mag/<int:pk>", delete_mag, name="delete_mag"),
    path(r"delete_round_tube/<int:pk>", delete_round_tube, name="delete_round_tube"),
]
