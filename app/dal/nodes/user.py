from neomodel import StructuredNode, StringProperty, RelationshipTo
from .properties import ShortIdProperty
from .system import System


class User(StructuredNode):
    gagl_id = ShortIdProperty()
    discord_id = StringProperty(required=False)

    system = RelationshipTo(System, 'OWNS')

