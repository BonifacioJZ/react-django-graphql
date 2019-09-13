import graphene
from .types import Query as SchemaQuery
from .mutation import Mutation as MutationQuery
class Query(SchemaQuery, graphene.ObjectType):
    pass
class Mutation(MutationQuery,graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query,mutation=Mutation)