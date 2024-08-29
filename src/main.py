from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from app.notification.sms.routers import router as sms_routers
from app.integration.routers import router as integration_routers
from app.auth.routers import router as auth_routers
from app.utilities.helpers import validation_exception_handler

app = FastAPI(title="Conversia", version="1.0.0")
app.include_router(integration_routers, prefix="/noti/v1",tags=["Integrations"])
app.include_router(sms_routers, prefix="/noti/v1",tags=["SMS"])
app.include_router(auth_routers, prefix="/auth/v1",tags=["Auth"])

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Conversia",
        version="1.0.0",
        routes=app.routes,
        servers=[{"url": "/"}],
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.get("/")
def root():
    return {"message": "Bienvenido al backend"}