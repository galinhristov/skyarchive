from django.urls import path
from .views import (
    role_list,
    role_create,
    role_details,
    role_edit,
    role_delete,
    manufacturer_list,
    country_list,
)

urlpatterns = [
    path('roles/', role_list, name='role_list'),
    path('roles/create/', role_create, name='role_create'),
    path('roles/<int:pk>/', role_details, name='role_details'),
    path('roles/<int:pk>/edit/', role_edit, name='role_edit'),
    path('roles/<int:pk>/delete/', role_delete, name='role_delete'),
    path('manufacturers/', manufacturer_list, name='manufacturer_list'),
    path('countries/', country_list, name='country_list'),
]
