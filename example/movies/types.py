#En este archivo van todos los esquemas para GraphQL
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Actor, Movie
#Creando un type GraphQl para el modelo actor
class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

#Creando a GraphQl para el modelo Movie
class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
#Crearcion de querys types
class Query(ObjectType):
#Select * from Actor where id = actor.id
    actor = graphene.Field(ActorType,id = graphene.Int())
#Select * from Movie where id = movie.id
    movie = graphene.Field(MovieType,id = graphene.Int())
#Select * from Actor 
    actors = graphene.List(ActorType)
#Select * from Movie
    movies = graphene.List(MovieType)

#Estos son los resolver de las Querys
    def resolve_actor(self,info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Actor.objects.get(pk=id)
        return None 
    def resolve_movie(self,info,**kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Movie.objects.get(pk=id)
        return None
    def resolve_actors(self,info, **kwargs):
        return Actor.objects.all()
    def resolve_movies(self,info,**kwargs):
        return Movie.objects.all()    