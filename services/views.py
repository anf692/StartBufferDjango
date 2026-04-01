from django.shortcuts import render
from .models import Traiteurs
# Create your views here.

def list_traiteur(request):
    traiteur = Traiteurs.objects.all()
    context = {
        "traiteur_list" : traiteur
    }

    return render(request, "liste.html", context)