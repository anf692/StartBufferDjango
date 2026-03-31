from django.db import models

# Create your models here.
class Specialites(models.Model):
    nomspecialite = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomspecialite
        


class Traiteurs(models.Model):
    nomcomplet = models.CharField(max_length=100)
    specialite = models.ManyToManyField(Specialites)
    description = models.TextField()
    adresse = models.CharField(max_length=20)
    est_actif = models.BooleanField(default=False)
    email = models.EmailField()
    datedecreation = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=20)
    image = models.URLField( blank=True, null=True)
    
    def __str__(self):
        return self.nomcomplet