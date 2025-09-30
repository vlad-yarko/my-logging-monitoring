from sqlalchemy import Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class MyDBModel(Base):
    __tablename__ = "my_db"

    title: Mapped[str] = mapped_column(Text)
