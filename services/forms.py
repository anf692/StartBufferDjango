from django import forms
from .models import Traiteurs


class traiteurform(forms.ModelForm):
    class Meta:
        model = Traiteurs
        fields = ("nomcomplet", "email", "specialite", "description", "telephone", "adresse", "image")
