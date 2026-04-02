from django.shortcuts import render, get_object_or_404
from .models import Traiteurs
from django.shortcuts import render
from .models import Traiteurs
from .forms import traiteurform
from django.contrib.auth.decorators import login_required

# Cette ligne empêche l'accès si l'utilisateur n'est pas connecté
@login_required(login_url='/comptes/login/')
def list_traiteur(request):
    traiteur = Traiteurs.objects.all()
    context = {
        "traiteur_list": traiteur
    }
    return render(request, "liste.html", context)



def detail_traiteur(request, pk):
    traiteur = get_object_or_404(Traiteurs, pk=pk)
    return render(request, "detail-traiteur.html", {"traiteur": traiteur})


def acceuil(request):
    return render(request, "index.html")

def formulaire(request):
    return render(request, "forms.html")

def traiteur_page_view(request):
    succes_msg = None
    if request.method == "POST":
        form = traiteurform(request.POST)
        if form.is_valid():
            form.save()
            succes_msg = "Votre message a bien ete envoyer avec succes"
            form = traiteurform()
    else:
        form = traiteurform()
    context = {
        "form" : form,
        "succes_msg" : succes_msg
    }
    return render(request, "forms.html", context)
# from django.contrib.auth.decorators import login_required

# @login_required # Applique le décorateur juste avant la définition
# def ma_vue_protegee(request):
#    # ...
#    return render(request, 'login.html')