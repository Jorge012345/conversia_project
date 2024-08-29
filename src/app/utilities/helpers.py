from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    error = errors[0]
    field = error["loc"][1] if len(error["loc"]) > 1 else error["loc"][0]
    error_type = error["type"]
    if error_type == "string_type":
        detail = f"El campo '{field}' debe ser una cadena de caracteres."
    elif error_type == "missing":
        detail = f"El campo '{field}' es obligatorio."
    elif error_type == "url_parsing":
        detail = f"El campo '{field}' debe ser un valor URL válido."
    else:
        detail = "Ha ocurrido un error de validación en la solicitud."

    return JSONResponse(
                status_code=400,
                content={"description": detail},
            )