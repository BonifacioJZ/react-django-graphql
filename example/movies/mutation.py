from graphene  import ObjectType
from .queryM import CreateActor,UpdateActor,DeleteActor,CreateMovie,UpdateMovie

class Mutation(ObjectType):
    #Creations
    create_actor=CreateActor.Field()
    create_movie=CreateMovie.Field()
    #Updates
    update_movie=UpdateMovie.Field()
    update_actor=UpdateActor.Field()
    #Deletes
    delete_actor=DeleteActor.Field() 
    
    