from neomodel import StringProperty, RelationshipTo, RelationshipFrom, One

from ._base import ConfigurableNode


class System(ConfigurableNode):
    name = StringProperty(required=True, index=True)
    description = StringProperty(required=False)

    user = RelationshipFrom('app.dal.nodes.user.User', 'OWNS', One)
    subsystems = RelationshipTo('System', 'SUBSYSTEM')
