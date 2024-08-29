from sqlalchemy import Column, String, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime, timezone

Base = declarative_base()


class Integration(Base):
    __tablename__ = 'integrations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    description = Column(String)
    endpoint = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    access_token = Column(String)