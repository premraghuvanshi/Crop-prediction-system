import os
from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker

DB_URL=os.getenv("DB_URL")

if not DB_URL:
    raise RuntimeError("DB_URL environment variable is not set.")

engine = create_async_engine(
    DB_URL,
    pool_size=30,
    max_overflow=15,
    pool_recycle=1800,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        
        finally : 
            
            pass