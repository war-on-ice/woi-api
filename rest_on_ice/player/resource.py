from flask_restful import Resource
from flask_test.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
)
from flask_test.player.model import Player

from flask_test.player.base_resource import BaseResource

class PlayerResource(BaseResource):
    def __init__(self):
        BaseResource(resource_class = Player, primary_key='ID')
