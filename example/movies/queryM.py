import graphene
from .inputs import ActorInput,MovieInput
from .models import Actor,Movie
from .types import ActorType,MovieType
#mutaciones para Actor
class CreateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required=True)
    ok = graphene.Boolean()
    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root,info,input=None):
        ok = True 
        actor_instance = Actor(name=input.name)
        actor_instance.save()
        return CreateActor(ok=ok, actor=actor_instance)

class UpdateActor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ActorInput(required=True)
    
    ok = graphene.Boolean()
    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        actor_instance = Actor.objects.get(pk=id)
        if actor_instance:
            ok = True
            actor_instance.name = input.name
            actor_instance.save()
            return UpdateActor(ok=ok, actor=actor_instance)
        return UpdateActor(ok=ok,actor=None)

class DeleteActor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root,info,id):
        ok = False
        actor_instance = Actor.objects.get(pk = id)
        if actor_instance:
            ok = True
            actor_instance.delete()
            return DeleteActor(ok=ok)
        return DeleteActor(ok=ok)
class CreateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)
    ok = graphene.Boolean()
    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        actors = []
        for actor_input in input.actors:
            
            actor = Actor.objects.get(pk= actor_input.id)
           
            if actor is None:
                return CreateMovie(ok=False,Movie=None)
            actors.append(actor)
        movie_instance = Movie(
            title=input.title,
            year=input.year
        )
        movie_instance.save()
        movie_instance.actors.set(actors)
        return CreateMovie(ok=ok,  movie=movie_instance)

class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MovieInput(required=True)
        
    ok= graphene.Boolean()
    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok=False
        movie_instance = Movie.objects.get(pk=id)
        if movie_instance:
            ok= True
            actors=[]
            for actor_input in input.actors:
                actor = Actor.objects.get(pk=actor_input.id)
                if actor is None:
                    return UpdateMovie(ok=False, movie=None)
                actors.append(actor)
            movie_instance.title=input.title
            movie_instance.year = input.year
            movie_instance.save()
            movie_instance.actors.set(actors)
            return UpdateMovie(ok=ok, movie=movie_instance)
        return UpdateMovie(ok=ok, movie=None)
