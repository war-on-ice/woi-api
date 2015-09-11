from flask_restful import Resource
from flask_test.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
)
from flask_test.player.model import Player
from flask_test.utils import row2dict

from flask_test.player.base_resource import BaseResource

class PlayerListResource(BaseResource):
    def __init__(self):
        super(PlayerListResource, self).__init__(resource_class=Player, primary_key='ID')

    def get(self):
        output = self._get_resource_list({})
        return [row2dict(x) for x in output]

class PlayerResource(BaseResource):
    def __init__(self):
        super(PlayerResource, self).__init__(resource_class=Player, primary_key='ID')

