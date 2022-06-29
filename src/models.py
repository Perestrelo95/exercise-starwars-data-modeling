import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Late_name = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)
    Date = Column(String(), nullable=False)
    Id_favorite_character = Column(Integer, ForeignKey('favorite_character.id'))
    favorite_character = relationship('Favorite_character')
    Id_favorite_planet = Column(Integer, ForeignKey('favorite_planet.id'))
    favorite_planet = relationship('Favorite_planet')

    
class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_planet = Column(Integer, primary_key=True)
    Details = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_character = Column(Integer, primary_key=True)
    Details = Column(String(250), nullable=False)

class Favorite_planet(Base):
    __tablename__ = 'favorite_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer,ForeignKey('id_planet.id'))
    planet = relationship(Planet)
    id_planet = Column(Integer,ForeignKey('planet.id'))
    planet = relationship(Planet)
    
class Favorite_character(Base):
    __tablename__ = 'favorite_character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer,ForeignKey('id_character.id'))
    character = relationship(Character)
    id_character = Column(Integer,ForeignKey('character.id'))
    character = relationship(Character)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')