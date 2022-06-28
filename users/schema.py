import graphene 
import graphene_django 

from graphql_auth import mutations


class AuthMutations(graphene.ObjectType):
    register = mutations.Register.Field()
