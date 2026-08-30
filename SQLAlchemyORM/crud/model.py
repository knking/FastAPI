from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Table, Column
from db import engine


class Base(DeclarativeBase):
    pass



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


    # One-to-Many: User -> Post
    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete"
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

    def __repr__(self) -> str:
        return f"<Post(id={self.id}, title={self.title}, user_id={self.user_id})>"

def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)