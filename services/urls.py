from django.urls import path
from .views import accueil, liste_traiteurs, detail_traiteur, SignupView, ajouter_traiteur, contact


urlpatterns = [
    path('', accueil, name='accueil'),
    path('liste/', liste_traiteurs, name='liste_traiteurs'),
    path('traiteurs/<int:id>/', detail_traiteur, name='detailtraiteur'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('ajouter/', ajouter_traiteur, name='ajouter_traiteur'),
    path('contact/', contact, name='contact'),
]
