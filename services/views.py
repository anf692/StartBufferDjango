from django.shortcuts import render, get_object_or_404, redirect
from .models import Traiteurs, Specialites
from .forms import TraiteurForm

# Authentification
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#loginrequired
from django.contrib.auth.decorators import login_required


def accueil(request):
    return render(request, 'index.html')


# Cette ligne empêche l'accès si l'utilisateur n'est pas connecté
@login_required
def liste_traiteurs(request):
    traiteurs = Traiteurs.objects.all()
    specialites = Specialites.objects.all()

    # récupérer les valeurs
    specialite = request.GET.get('specialite')
    statut = request.GET.get('statut')

    # filtrer spécialité
    if specialite:
        traiteurs = traiteurs.filter(specialite__id=specialite)

    # filtrer statut
    if statut == "actif":
        traiteurs = traiteurs.filter(est_actif=True)
    elif statut == "inactif":
        traiteurs = traiteurs.filter(est_actif=False)

    return render(request, 'traiteur.html', {
        'traiteurs': traiteurs,
        'specialites': specialites
    })


def detail_traiteur(request, id):
    traiteur = get_object_or_404(Traiteurs, id=id)
    return render(request, "detail.html", {"traiteur": traiteur})



class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


from django.contrib.auth.decorators import login_required

@login_required
def ajouter_traiteur(request):
    if request.method == 'POST':
        form = TraiteurForm(request.POST, request.FILES)
        if form.is_valid():
            traiteur = form.save(commit=False) 
            traiteur.user = request.user    
            traiteur.save()                  

            return redirect('liste_traiteurs')
    else:
        form = TraiteurForm()

    return render(request, 'inscription-traiteur.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')

