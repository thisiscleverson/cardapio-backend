import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .db.config_db import ConfigDB, ConfigURI


app = Flask(__name__)
ConfigURI(app)
ConfigDB(app)
engine = Migrate(app, app.db)
CORS(app)


from .controllers.routes import * 