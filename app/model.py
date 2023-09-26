from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
   pass

db = SQLAlchemy(model_class=Base)

def config_db(app) -> None:
   db.init_app(app)
   app.db = db


class Foods(db.Model):
   __tablename__ = "foods"

   id:    Mapped[int] = mapped_column(String(36), primary_key=True)
   name:  Mapped[str] = mapped_column(String, unique=True, nullable=False)
   price: Mapped[int] = mapped_column(Integer)
   image: Mapped[str] = mapped_column(String)

   def __init__(self, id, name, price, image):
      self.id    = id
      self.name  = name
      self.price = price
      self.image = image