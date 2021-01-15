from neomodel import StructuredNode, StringProperty, BooleanProperty


class BotFeature(StructuredNode):
    name = StringProperty(required=True, index=True)
    kind = StringProperty(required=True)
    disabled_by_default = BooleanProperty(required=False, default=False)
