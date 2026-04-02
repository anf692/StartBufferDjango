from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = "services"

urlpatterns = [
    path("", views.acceuil, name="accueil"),
    path("traiteur/", views.list_traiteur, name="traiteur"),
    path("forms/", views.formulaire, name="formulaire"),
    path('comptes/logout/', auth_views.LogoutView.as_view(next_page='/index/traiteur/'), name='logout'),
    path("detail/<int:pk>/", views.detail_traiteur, name="detail"),
]

# Ajouter ceci pour le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)