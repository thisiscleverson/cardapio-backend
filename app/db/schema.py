from .config_db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Foods(db.Model):
   """Schema from table foods"""
   
   __tablename__ = "foods"

   id:    Mapped[int] = mapped_column(String(36), primary_key=True)
   name:  Mapped[str] = mapped_column(String, unique=True, nullable=False)
   price: Mapped[int] = mapped_column(Integer)
   image: Mapped[str] = mapped_column(String)

   def __init__(self, id: str, name: str, price: int, image: str) -> None:
      self.id    = id
      self.name  = name
      self.price = price
      self.image = image