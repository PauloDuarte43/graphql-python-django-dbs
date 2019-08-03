import graphene
from graphene_django import DjangoObjectType

from .models import Address


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class Query(graphene.ObjectType):
    addresses = graphene.List(AddressType)

    def resolve_addresses(self, info, **kwargs):
        return Address.objects.all()