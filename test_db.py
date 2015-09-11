# coding: utf-8
from flask_test.settings import ProdConfig
from flask_test.app import create_app
app = create_app(config_object=ProdConfig)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from flask_test.player.model import Player
Player()
