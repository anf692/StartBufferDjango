from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Specialites(models.Model):
    nomspecialite = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomspecialite
        


class Traiteurs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nomcomplet = models.CharField(max_length=100)
    specialite = models.ManyToManyField(Specialites)
    description = models.TextField()
    adresse = models.CharField(max_length=20)
    est_actif = models.BooleanField(default=False)
    email = models.EmailField()
    datedecreation = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='traiteurs/', blank=True, null=True)
    
    def __str__(self):
        return self.nomcomplet
