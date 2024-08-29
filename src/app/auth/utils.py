import jwt
import pytz
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from settings import Settings

SECRET_KEY = Settings.TOKEN


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/v1/token")


class Auth:

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        local_timezone = pytz.timezone('America/Lima')
        now = datetime.now(local_timezone)
        expire = now + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return encoded_jwt

    @staticmethod
    def validate_token(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            if not payload:
                raise HTTPException(status_code=401, detail="Invalid credentials")
            return True
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))