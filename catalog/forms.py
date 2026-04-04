from django import forms
from catalog.models import Role


class RoleBaseForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
        labels = {
            'name': 'Role Name',
            'description': 'Role Description',
        }
        help_texts = {
            'name': 'Example: Multirole Fighter',
            'description': 'Describe the purpose of this aircraft role.',
        }
        widgets = {
            'name': forms.Textarea(attrs={
                'placeholder': 'Enter role description',
                'rows': 4,
            }),
        }
        error_messages = {
            'name': {
                'unique': 'A role with this name already exists.',
                'required': 'Please enter a role name.',
            },
            'description': {
                'required': 'Please enter a description.',
            },
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name.strip()) < 2:
            raise forms.ValidationError('Role name must contain at least 2 characters.')
        return name.strip()

    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description.strip()) < 10:
            raise forms.ValidationError('Description must contain at least 10 characters.')
        return description.strip()


class RoleCreateForm(RoleBaseForm):
    pass


class RoleEditForm(RoleBaseForm):
    pass


class RoleDeleteForm(RoleBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


