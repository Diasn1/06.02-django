from django import forms
from .models import Animal, Enclosure

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'health_status']

class EnclosureForm(forms.ModelForm):
    class Meta:
        model = Enclosure
        fields = ['name', 'capacity', 'animals']