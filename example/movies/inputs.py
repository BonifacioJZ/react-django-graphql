import graphene

#Definiendo los datos de entrada para los modelos
class ActorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    actors = graphene.List(ActorInput)
    year = graphene.Int()
    