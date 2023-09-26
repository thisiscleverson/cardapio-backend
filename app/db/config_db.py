import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv())

DB_CONFIG = {
   "host":      os.getenv('HOST'),    
   "user":      os.getenv('USER'),
   "port":      os.getenv('PORT'),
   "database":  os.getenv('DB'),
   "password":  os.getenv('PASS')
}


db = SQLAlchemy()

class ConfigDB():
   def __init__(self, app) -> None:
      db.init_app(app)
      app.db = db


class ConfigURI():
   def __init__(self, app) -> None:
      app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_CONFIG["user"]}:{DB_CONFIG["password"]}@{DB_CONFIG["host"]}/{DB_CONFIG["database"]}'
      app.config['EXCTEND_EXISTING'] = True