from neomodel import StructuredNode, StringProperty, RelationshipTo
from .properties import ShortIdProperty


class System(StructuredNode):
    name = StringProperty(required=True, index=True)
    description = StringProperty(required=False)

    subsystems = RelationshipTo('System', 'SUBSYSTEM')
