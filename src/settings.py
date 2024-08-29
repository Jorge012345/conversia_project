from starlette.config import Config

class Settings:
    config = Config(".env")
    DATABASE_URL = config("DATABASE_URL", default="postgresql+psycopg://postgres:postgres@localhost/conversia")
    TWILIO_ENDPOINT_SEND_SMS = config("TWILIO_ENDPOINT_SEND_SMS", default="https://api.twilio.com/send-sms")
    TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID", default="default_sid")
    TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN", default="default_auth_token")
    SERVICE_URL = config("SERVICE_URL", default="http://localhost:8000")
    TOKEN = config("TOKEN", default="default_token")