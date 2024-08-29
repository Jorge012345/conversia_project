import httpx
import asyncio
from fastapi import APIRouter, Depends, status
from settings import Settings
from app.integration.schemas import Integration
from fastapi.responses import JSONResponse
from app.auth.utils import Auth

router = APIRouter()

@router.post("/send-sms/{integration_id}", status_code=status.HTTP_200_OK)
async def send_sms_twilio(integration_id: str, token: str = Depends(Auth.validate_token)):
    async with httpx.AsyncClient() as client:
        try:
            integration_response = await client.get(f"{Settings.SERVICE_URL}/noti/v1/integrations/{integration_id}")
            if integration_response.status_code != 200:
                return JSONResponse(
                    status_code=404,
                    content={
                        "description": f"Integration not found."
                    },
                )
            integration = Integration(**integration_response.json())
            task = asyncio.create_task(client.post(
                integration.endpoint,
                headers={"Authorization": f"Bearer {integration.access_token}"},
                json={"message": "Hello, World!"},
            ))
            await task

            return JSONResponse(
                status_code=200,
                content={
                    "description": "SMS sent successfully"
                },
            )
        except httpx.ReadTimeout:
            return JSONResponse(
                status_code=504,
                content={"description": "The server took too long to respond."}
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={
                    "description": f"Error to send SMS: {str(e)}"
                },
            )