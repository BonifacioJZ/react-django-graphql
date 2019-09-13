from django.db import models

# Create your models here.
#creacion de los modelos para el ejemplo con graphql
#Modelo de Actor
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#Modelo de Pelicula
class Movie(models.Model):
    title = models.CharField(max_length=100)
#Relacion muchos a muchos con la Tabla actor
    actors = models.ManyToManyField(Actor)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    
        