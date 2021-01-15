from neomodel import StringProperty, RelationshipTo, StructuredNode, ZeroOrOne, UniqueIdProperty

from .properties import ShortIdProperty
from .system import System


class User(StructuredNode):
    gagl_id = ShortIdProperty()
    discord_id = StringProperty(required=False)
    api_token = UniqueIdProperty()

    systems = RelationshipTo(System, 'OWNS')
    settings = RelationshipTo('app.dal.nodes.settings.UserSettings', 'SETTINGS', ZeroOrOne)

    @property
    def all_systems(self):
        q = 'MATCH (u:User) WHERE id(u)=$self MATCH (u)-[:OWNS]->(x)-[:SUBSYSTEM|MEMBER*0..]-(ss:System) RETURN ss'
        results, columns = self.cypher(q)
        return [System.inflate(row[-1]) for row in results]
