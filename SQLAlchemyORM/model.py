
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from db import engine

class Base(DeclarativeBase):
    pass

# User Model(User table)

class user(Base):
    __tablename__="users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]= mapped_column(String(length=50), nullable=False)
    email: Mapped[str]=mapped_column(String, unique=True, nullable=False)
    phone:Mapped[str]=mapped_column(Integer, unique=True, nullable=False)


    def __repr__(self) -> str:
        return f"<User(id={self.id},name={self.name},email={self.email})>"

class Address(Base):
    __tablename__="address"

    id:Mapped[int] = mapped_column(primary_key=True)
    city:Mapped[str]= mapped_column(String(length=15), nullable=False)
    pin:Mapped[int]= mapped_column(Integer, nullable=False)


    def __repr__(self) -> str:
            return f"<Address(id={self.id},city={self.cityame},pin={self.pin})>"

def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)