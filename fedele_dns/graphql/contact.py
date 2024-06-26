from graphene import ObjectType

from netbox.graphql.fields import ObjectField, ObjectListField
from netbox.graphql.types import NetBoxObjectType

from fedele_dns.models import Contact
from fedele_dns.filters import ContactFilter


class ContactType(NetBoxObjectType):
    class Meta:
        model = Contact
        fields = "__all__"
        filterset_class = ContactFilter


class ContactQuery(ObjectType):
    contact = ObjectField(ContactType)
    contact_list = ObjectListField(ContactType)
