from neomodel import StructuredNode, StringProperty, RelationshipTo
from .properties import ShortIdProperty
from .system import System


class User(StructuredNode):
    gagl_id = ShortIdProperty()
    discord_id = StringProperty(required=False)

    systems = RelationshipTo(System, 'OWNS')

    @property
    def all_systems(self):
        q = 'MATCH (u:User) WHERE id(u)=$self MATCH (u)-[:OWNS]->(x)-[:SUBSYSTEM|MEMBER*0..]-(ss:System) RETURN ss'
        results, columns = self.cypher(q)
        return [System.inflate(row[-1]) for row in results]

