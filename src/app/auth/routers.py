from fastapi import APIRouter, HTTPException, status
from app.auth.utils import Auth
from datetime import timedelta
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/token")
def login():
    try:
        access_token_expires = timedelta(minutes=1)
        access_token = Auth.create_access_token(
            data={"sub": "value"}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        return JSONResponse(
                status_code=500,
                content={
                    "description": f"Error login: {str(e)}"
                },
            )