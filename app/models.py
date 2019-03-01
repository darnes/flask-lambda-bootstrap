from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

from app import db


class CustomUnusedModel(db.Model):
    """
    Model Detail description
    """
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
