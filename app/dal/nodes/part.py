from neomodel import StringProperty, RelationshipTo, StructuredRel, IntegerProperty, ArrayProperty, \
    DateProperty, JSONProperty

from ._base import ConfigurableNode


class NetworkRel(StructuredRel):
    basic_type = StringProperty()  # familial, platonic, romantic, etc
    specific_type = StringProperty()  # user specified
    since = DateProperty(required=False)
    details = StringProperty(required=False)


class Part(ConfigurableNode):
    name = StringProperty(required=True, index=True)
    description = StringProperty(required=False)
    pronouns = StringProperty(required=False)
    role = StringProperty(required=False)
    birthday = DateProperty(required=False)
    age_lower = IntegerProperty(required=False)  # for age sliders
    age_upper = IntegerProperty(required=False)  # for age sliders
    age = IntegerProperty(required=False)
    kind = StringProperty(required=False)  # for specifying non-human subtype, e.g. species or type of object
    appearance = StringProperty(required=False)  # written notes about appearance - images set elsewhere
    beliefs = StringProperty(required=False)  # religion/spirituality
    tells = ArrayProperty(required=False)
    likes = ArrayProperty(required=False)
    dislikes = ArrayProperty(required=False)
    positive_triggers = ArrayProperty(required=False)
    negative_triggers = ArrayProperty(required=False)
    additional = JSONProperty(required=False)  # anything else

    subsystem = RelationshipTo('app.dal.nodes.system.System', 'SUBSYSTEM')
    system = RelationshipTo('app.dal.nodes.system.System', 'MEMBER')
    network = RelationshipTo('Part', 'NETWORK', model=NetworkRel)

    def _add_network(self, other, basic_type, specific_type, since=None, details=None, reciprocal=None):
        properties = {'basic_type': basic_type,
                      'specific_type': specific_type,
                      'since': since,
                      'details': details}
        self.network.connect(other, properties)
        if reciprocal is not None:
            properties['specific_type'] = reciprocal
            other.network.connect(self, properties)

    def add_family(self, other, relationship_type, since=None, details=None, reciprocal=None):
        self._add_network(other, 'familial', relationship_type, since, details, reciprocal)

    def add_friend(self, other, relationship_type='friend', since=None, details=None, reciprocal='friend'):
        self._add_network(other, 'platonic', relationship_type, since, details, reciprocal)

    def add_partner(self, other, relationship_type='partner', since=None, details=None, reciprocal='partner'):
        self._add_network(other, 'romantic', relationship_type, since, details, reciprocal)

    @property
    def family(self):
        q = 'MATCH (p:Part) WHERE id(p)=$self MATCH (p)-[n:NETWORK{basic_type:"familial"}]-(pp:Part) RETURN n, pp'
        results, columns = self.cypher(q)
        family = {}
        for n, pp in results:
            relationship = NetworkRel.inflate(n)
            part = Part.inflate(pp)
            entry = family.get(part.id, {'part': part, 'relationships': []})
            entry['relationships'] += [relationship]
            family[part.id] = entry
        return family
