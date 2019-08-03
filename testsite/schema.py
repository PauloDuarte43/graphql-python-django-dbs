import graphene

import users.schema
import customers.schema


class Query(
        users.schema.Query, 
        customers.schema.Query, 
        graphene.ObjectType
    ):
    pass


schema = graphene.Schema(query=Query)