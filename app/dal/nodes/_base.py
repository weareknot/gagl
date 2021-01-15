from neomodel import StructuredNode, RelationshipTo, ZeroOrOne


class ConfigurableNode(StructuredNode):
    """
    Just for inheriting from.
    """
    settings = RelationshipTo('app.dal.nodes.settings.ConfigurableNodeSettings', 'SETTINGS', ZeroOrOne)
