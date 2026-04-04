from django import forms

from aircrafts.models import Aircraft


class AircraftBaseForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        fields = [
            'name',
            'image_url',
            'description',
            'first_flight_year',
            'max_speed_kmh',
            'crew',
            'is_active_service',
            'role',
            'manufacturers',
            'origin_countries',
            'features',
        ]
        labels = {
            'name': 'Aircraft Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'first_flight_year': 'First Flight Year',
            'max_speed_kmh': 'Max speed (km/h)',
            'crew': 'Crew Members',
            'is_active_service': 'Currently in Active Service',
            'role': 'Role',
            'manufacturers': 'Manufacturers',
            'origin_countries': 'Origin Countries',
            'features': 'Special Features',
        }
        help_texts = {
            'name': 'Example: F-16C Fighting Falcon',
            'description': 'Write a short summary of the aircraft.',
            'first_flight_year': 'Enter the year of the first flight.',
            'max_speed_kmh': 'Use numbers only.',
            'crew': 'Enter the number of crew members.',
            'features': 'You may leave this field empty.',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter aircraft name',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'https://example.com/image.jpg',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter aircraft description',
                'rows': 5,
            }),
            'first_flight_year': forms.NumberInput(attrs={
                'placeholder': 'e.g. 2400',
            }),
            'crew': forms.NumberInput(attrs={
                'placeholder': 'e.g. 1 or 2',
            }),
        }
        error_messages = {
            'name': {
                'unique': 'An aircraft with this name already exists.',
                'required': 'Please enter an aircraft  name.',
            },
            'image_url': {
                'required': 'Please provide an image URL.',
                'invalid': 'Please enter a valid URL',
            },
            'description': {
                'required': 'Please enter a description.',
            },
            'first_flight_year': {
                'required': 'Please enter the first flight year.',
            },
            'max_speed_kmh': {
                'required': 'Please enter the maximum speed.',
            },
            'crew': {
                'required': 'Please enter the crew count.',
            },
            'role': {
                'required': 'Please choose a role.',
            },
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name.strip()) < 2:
            raise forms.ValidationError('Aircraft name must contain at least 2 characters.')
        return name.strip()

    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description.strip()) < 20:
            raise forms.ValidationError('Description must contain at least 20 characters.')
        return description.strip()


class AircraftCreateForm(AircraftBaseForm):
    pass



class AircraftEditForm(AircraftBaseForm):
    pass



class AircraftDeleteForm(AircraftBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance














