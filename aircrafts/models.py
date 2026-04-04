from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from catalog.models import Role, Manufacturer, Country, Feature


class Aircraft(models.Model):
    NAME_MAX_LENGTH = 100
    MIN_DESCRIPTION_LENGTH = 20
    FIRST_FLIGHT_YEAR_MIN_VALUE = 1903
    MAX_SPEED_MIN_VALUE = 100
    CREW_MIN_VALUE = 1

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(2),
        ),
        help_text="Example: F-16C Fighting Falcon",
    )
    image_url = models.URLField(
        verbose_name="Image URL",
    )
    description = models.TextField(
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        help_text="Write at least 20 characters.",
    )
    first_flight_year = models.PositiveIntegerField(
        validators=(
            MinValueValidator(FIRST_FLIGHT_YEAR_MIN_VALUE),
        ),
    )
    max_speed_kmh = models.PositiveIntegerField(
        verbose_name="Max speed (km/h)",
        validators=(
            MinValueValidator(MAX_SPEED_MIN_VALUE),
        ),
    )
    crew = models.PositiveIntegerField(
        validators=(
            MinValueValidator(CREW_MIN_VALUE),
        ),
    )
    is_active_service = models.BooleanField(
        default=True,
    )
    role = models.ForeignKey(
        to='catalog.Role',
        on_delete=models.CASCADE,
        related_name="aircraft",
    )
    manufacturers = models.ManyToManyField(
        to='catalog.Manufacturer',
        related_name="aircraft",
    )
    origin_countries = models.ManyToManyField(
        to='catalog.Country',
        related_name="origin_aircraft",
    )
    features = models.ManyToManyField(
        to='catalog.Feature',
        related_name="aircraft",
        blank=True,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def clean(self):
        current_year = date.today().year

        if self.first_flight_year > current_year:
            raise ValidationError({
                "first_flight_year": "First flight year cannot be in the future."
            })

