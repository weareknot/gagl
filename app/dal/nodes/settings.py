from neomodel import StructuredNode, RelationshipTo, RelationshipFrom, One, StringProperty


class Settings(StructuredNode):
    disabled_features = RelationshipTo('app.dal.nodes.bot_feature.BotFeature', 'DISABLED')


class UserSettings(Settings):
    user = RelationshipFrom('app.dal.nodes.user.User', 'SETTINGS', One)
    disabled_servers = RelationshipTo('ServerSettings', 'DISABLED')


class ServerSettings(Settings):
    server = RelationshipFrom('app.dal.nodes.server.Server', 'SETTINGS', One)
    blocklisted_users = RelationshipTo('UserSettings', 'BLOCKLIST')


class ConfigurableNodeSettings(Settings):
    display_name = StringProperty(required=False)
    avatar = StringProperty(required=False)
    proxy_tag = StringProperty(required=False)
    autoproxy = StringProperty(required=False)
    entity = RelationshipFrom('app.dal.nodes._base.ConfigurableNode', 'SETTINGS', One)
    scope = RelationshipTo('app.dal.nodes.server.Server', 'SCOPE')
