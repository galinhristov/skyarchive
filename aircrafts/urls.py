from django.urls import path
from .views import (
    aircraft_list,
    aircraft_create,
    aircraft_details,
    aircraft_edit,
    aircraft_delete,
    aircraft_filter,
)

urlpatterns = [
    path('', aircraft_list, name='aircraft_list'),
    path('create/', aircraft_create, name='aircraft_create'),
    path('filter/', aircraft_filter, name='aircraft_filter'),
    path('<int:pk>/', aircraft_details, name='aircraft_details'),
    path('<int:pk>/edit/', aircraft_edit, name='aircraft_edit'),
    path('<int:pk>/delete/', aircraft_delete, name='aircraft_delete'),

]
