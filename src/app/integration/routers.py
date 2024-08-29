from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.integration.services import get_integration, post_integration
from app.integration import schemas as IntegrationSchemas
router = APIRouter()

@router.get("/integrations/{integration_id}", status_code=status.HTTP_200_OK, response_model=IntegrationSchemas.Integration)
async def read_integration(integration_id: str):
    try:
        integration = await get_integration(integration_id)
        if not integration:
            return JSONResponse(
                    status_code=404,
                    content={
                        "description": "Integration not found."
                    },
                )
        return integration
    except Exception as e:
        return JSONResponse(
                status_code=500,
                content={
                    "description": f"Error getting integration: {str(e)}"
                },
            )

@router.post("/integrations",  status_code=status.HTTP_201_CREATED, response_model=IntegrationSchemas.Integration)
async def create_integration(integration: IntegrationSchemas.IntegrationCreate):
    try:
        new_integration = await post_integration(integration)
        if not integration:
            raise Exception("Integration creation failed. The result is None.")
        return new_integration
    except Exception as e:
        return JSONResponse(
                status_code=500,
                content={
                    "description": f"Error creating integration: {str(e)}"
                },
            )
    