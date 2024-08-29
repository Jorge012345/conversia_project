from sqlalchemy.orm import Session
from src.app.notification.sms.models import Integration



def get_integration(db: Session, integration_id: int):
    return db.query(Integration).filter(Integration.id == integration_id).first()