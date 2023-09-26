import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .model import config_db, db


load_dotenv()
HOST  = os.getenv('HOST') 
PORT  = os.getenv('PORT')
USER  = os.getenv('USER')
PASS  = os.getenv('PASS')
DB    = os.getenv('DB')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USER}:{PASS}@{HOST}/{DB}'
app.config['EXCTEND_EXISTING'] = True

config_db(app)
engine = Migrate(app, app.db)

with app.app_context():
    db.create_all()

CORS(app)


from .controllers.routes import * 


