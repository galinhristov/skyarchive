from django.contrib import admin

from aircrafts.models import Aircraft


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role',
        'first_flight_year',
        'crew',
        'is_active_service'
    )
    list_filter = (
        'role',
        'is_active_service',
        'first_flight_year',
    )
    search_fields = (
        'name',
        'description',
    )
    ordering = ('name',)
    filter_horizontal = (
        'manufacturers',
        'origin_countries',
        'features',
    )