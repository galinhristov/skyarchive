from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

class Country(models.Model):
    NAME_MAX_LENGTH = 56
    CODE_MAX_LENGTH = 3

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(2),
        ),
    )
    code = models.CharField(
        max_length=CODE_MAX_LENGTH,
        unique=True,
        blank=True,
        null=True,
        validators=(
            MinLengthValidator(2),
            MaxLengthValidator(3),
        ),
        help_text="Optional country code, e.g. US, UK, DE.",
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name



class Manufacturer(models.Model):
    NAME_MAX_LENGTH = 80

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(2),
        ),
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    countries = models.ManyToManyField(
        to=Country,
        related_name='manufacturers',
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Role(models.Model):
    NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(2),
        ),
    )
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Feature(models.Model):
    NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(2),
        ),
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
