#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from models.user import User
import os

environment = os.environ.get("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if environment == "db":
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
