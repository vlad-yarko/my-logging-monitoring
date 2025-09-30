import asyncio

from dotenv import load_dotenv, find_dotenv

from engine import engine
from models import Base


load_dotenv(find_dotenv())


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_models())
