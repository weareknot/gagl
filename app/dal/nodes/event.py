from neomodel import StructuredNode, StringProperty, DateTimeProperty, StructuredRel, RelationshipFrom


class EventRel(StructuredRel):
    involvement = StringProperty(required=False)
    details = StringProperty(required=False)


class Event(StructuredNode):
    kind = StringProperty(required=True)
    description = StringProperty(required=False)
    when = DateTimeProperty(required=False)

    entities = RelationshipFrom(StructuredNode, 'INVOLVED', model=EventRel)


class Switch(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = 'switch'

