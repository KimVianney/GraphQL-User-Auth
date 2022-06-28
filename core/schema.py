import graphene

from graphql_auth.schema import UserQuery, MeQuery

import users.schema


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass
 


class Mutation(users.schema.AuthMutations, graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)
