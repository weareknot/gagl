from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, One


class Server(StructuredNode):
    name = StringProperty(required=True, index=True)

    users = RelationshipFrom('app.dal.nodes.user.User', 'MEMBER')
    settings = RelationshipTo('app.dal.nodes.settings.ServerSettings', 'SETTINGS', One)
