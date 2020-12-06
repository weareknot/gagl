from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, One


class System(StructuredNode):
    name = StringProperty(required=True, index=True)
    description = StringProperty(required=False)

    user = RelationshipFrom('app.dal.nodes.user.User', 'OWNS', One)
    subsystems = RelationshipTo('System', 'SUBSYSTEM')
