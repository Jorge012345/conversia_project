from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, HttpUrl

class IntegrationCreate(BaseModel):
    name: str
    description: str
    endpoint: HttpUrl
    access_token: str

class Integration(BaseModel):
    id: UUID
    name: str
    description: str
    endpoint: str
    created_at: datetime
    updated_at: datetime
    access_token: str

