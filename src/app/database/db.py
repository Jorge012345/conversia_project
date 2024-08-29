from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import Settings

class Database:
    DATABASE_URL = Settings.DATABASE_URL
    
    engine = create_async_engine(DATABASE_URL, echo=True)
    SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    Base = declarative_base()

    @staticmethod
    async def get_db():
        """Dependencia para obtener la sesión de base de datos."""
        async with Database.SessionLocal() as session:
            try:
                yield session
            finally:
                await session.close()