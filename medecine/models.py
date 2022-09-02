from email import message
from unittest.util import _MAX_LENGTH
from django.db import models


class Banner(models.Model):
    image =  models.FileField(upload_to="image_banner")
    description = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class About(models.Model):
    image = models.FileField()
    description = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    libelle = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class Our(models.Model):
    image = models.FileField()
    description = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    

class Team(models.Model):
    image = models.FileField()
    description = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    libelle = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class Contact(models.Model):
    nom = models.CharField(max_length=50,)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=100)
    telefone = models.IntegerField(default=1, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)





