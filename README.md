# StartBuffet

Application web Django pour présenter des traiteurs, leurs spécialités et permettre l’inscription de nouveaux profils.

**Stack :** projet développé avec la **dernière version stable de [Django](https://www.djangoproject.com/)** (installer via `pip` pour rester à jour).

## Fonctionnalités

- Page d’accueil et liste des traiteurs
- Fiche détaillée par traiteur (spécialités, description, contact, image)
- Formulaire de contact
- Inscription utilisateur (`/signup/`) et connexion / déconnexion via les comptes Django (`/comptes/login/`, etc.)
- Ajout d’un traiteur par les utilisateurs autorisés (`/ajouter/`)

## Prérequis

- Python 3.10 ou supérieur (recommandé ; vérifier la [compatibilité Python / Django](https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django) pour la version installée)
- **Django** — dernière version stable ([documentation](https://docs.djangoproject.com/en/stable/))
- **Pillow** — nécessaire pour le champ `ImageField` sur les traiteurs

## Installation

```bash
cd StartBuffet
python -m venv venv
```

Sous Windows (PowerShell) :

```powershell
.\venv\Scripts\Activate.ps1
```

Sous Linux ou macOS :

```bash
source venv/bin/activate
```

Installer les dépendances (Django et Pillow à jour) :

```bash
pip install -U django Pillow
```

## Configuration et lancement

1. Appliquer les migrations :

   ```bash
   python manage.py migrate
   ```

2. Créer un superutilisateur pour l’administration :

   ```bash
   python manage.py createsuperuser
   ```

3. Lancer le serveur de développement :

   ```bash
   python manage.py runserver
   ```

4. Ouvrir le navigateur sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
   Interface d’administration : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Structure utile

| Élément | Rôle |
|--------|------|
| `config/` | Paramètres du projet (`settings.py`, `urls.py`) |
| `services/` | Application métier (modèles `Traiteurs`, `Specialites`, vues, templates) |
| `templates/` | Templates globaux (base, authentification) |
| `static/` | Fichiers statiques partagés |
| `media/` | Fichiers uploadés (images des traiteurs), servis en mode `DEBUG` |

La base de données par défaut est **SQLite** (`db.sqlite3` à la racine du projet).

## Notes

- En production, définir `DEBUG = False`, une `SECRET_KEY` sécurisée, `ALLOWED_HOSTS`, et servir les fichiers médias/static de façon appropriée.
- Les redirections après connexion / déconnexion sont configurées dans `config/settings.py` (`LOGIN_REDIRECT_URL`, etc.).

