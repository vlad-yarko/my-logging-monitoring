import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_async_engine(   
    DATABASE_URL
)
main_session = async_sessionmaker(autocommit=False, bind=engine)
