from sqlalchemy.future import select
from .models import Integration
from app.integration import schemas as IntegrationSchemas
from app.database.db import Database

async def get_integration(integration_id: str):
    async for db in Database.get_db():
        try:
            result = await db.execute(select(Integration).where(Integration.id == integration_id))
            return result.scalars().first()
        except Exception as e:
            print("e: ",e)
            return None
        
async def post_integration(integration: IntegrationSchemas.IntegrationCreate):
    async for db in Database.get_db():
        new_integration = Integration(
            name=integration.name,
            description=integration.description,
            endpoint=str(integration.endpoint),
            access_token=integration.access_token,
        )
        db.add(new_integration)
        try:
            await db.commit()
            await db.refresh(new_integration)
            return new_integration
        except Exception as e:
            print("e: ",e)
            await db.rollback()
            return None