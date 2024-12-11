from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'keep_existing': True}                           #удобно наследовать для вывода
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')      #связь один ко многим

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))