import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(16), unique=True, nullable=False)
    password = Column(String(36), unique=False, nullable = False)

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            # do not serialize the password, its a security breach
        }

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Person = Column(String(16), nullable=False)
    planets = Column(String(36), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name
        }


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birthyear = Column(String(64))
    eye_color = Column(String(32))
    gender = Column(String(16))
    height = Column(Integer)
    mass = Column(Integer)

    def serialize(self):
        return {
            "height": self.height,
            "mass": self.mass,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "name" : self.name            
        }


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotational_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    
    def serialize(self):
        return {
            "diameter": self.height,
            "rotational_period": self.mass,
            "orbital_period": self.eye_color,
            "gravity": self.birth_year            
        }


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {"id": self.id,
    #         "name": self.name}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
