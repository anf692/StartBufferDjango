from django import forms
from .models import Traiteurs, Specialites

class TraiteurForm(forms.ModelForm):
    class Meta:
        model = Traiteurs
        fields = [
            'nomcomplet', 'specialite', 'description', 
            'adresse', 'est_actif', 'email', 'telephone', 'image'
        ]

        widgets = {
            'nomcomplet': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom complet'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Description'}),
            'adresse': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Adresse'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'telephone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Téléphone'}),
            'specialite': forms.CheckboxSelectMultiple(attrs={'class': 'select-multiple'}),
            'est_actif': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }