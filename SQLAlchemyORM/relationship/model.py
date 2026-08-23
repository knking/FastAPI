from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Table, Column
from db import engine


class Base(DeclarativeBase):
    pass


# Many-to-Many association table
user_address_association = Table(
    "user_address_association",
    Base.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "address_id",
        Integer,
        ForeignKey("address.id", ondelete="CASCADE"),
        primary_key=True
    )
)


# User Model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

    # One-to-Many: User -> Post
    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete"
    )

    # One-to-One: User -> Profile
    profile: Mapped["Profile"] = relationship(
        "Profile",
        back_populates="user",
        cascade="all, delete",
        uselist=False
    )

    # Many-to-Many: User -> Address
    addresses: Mapped[list["Address"]] = relationship(
        "Address",
        secondary=user_address_association,
        back_populates="users"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


# Post Model
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="posts"
    )


# Profile Model
class Profile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    bio: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="profile"
    )


# Address Model
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    street: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(15),
        nullable=False
    )

    users: Mapped[list["User"]] = relationship(
        "User",
        secondary=user_address_association,
        back_populates="addresses"
    )


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)