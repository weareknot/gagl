from neomodel import Property
from neomodel.properties import validator
import random
import string


class ShortIdProperty(Property):
    """
    Essentially exactly the same as UniqueIdProperty, just with a shorter default ID.
    """
    def __init__(self, **kwargs):
        for item in ['required', 'unique_index', 'index', 'default']:
            if item in kwargs:
                raise ValueError('{0} argument ignored by {1}'.format(item, self.__class__.__name__))

        kwargs['unique_index'] = True
        kwargs['default'] = lambda: u''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(6)])
        super(ShortIdProperty, self).__init__(**kwargs)

    @validator
    def inflate(self, value):
        return str(value)

    @validator
    def deflate(self, value):
        return str(value)
