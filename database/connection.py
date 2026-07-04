import os
from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker

DB_URL=os.getenv("DB_URL")

engine = create_async_engine(
    DB_URL,
    pool_size=30,
    max_overflow=15,
    pool_recycle=1800,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    with AsyncSessionLocal() as session:
        yield session