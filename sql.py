from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite://')
DBSession = sessionmaker(bind=engine)
session = DBSesssion()

Base = declarartive_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column('id',Integer,primary_key=True)
    name = Column('name',String(40))
    age = Column('age',Integer)

# create tables in the engine

Base.metadata.create_all(engine)

#Insert person

new_person = Person(name='Mary', age=30)
session.add(new_person)
new_person = Person(name='haris', age=27)
session.add(new_person)
session.commit()

for row in session.query(Person).all():
    print("{} is {} years old".format(row.name,row.age))
