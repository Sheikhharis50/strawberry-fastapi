from typing import Any

from fastapi import status
from fastapi.responses import JSONResponse


class APIResponse(JSONResponse):
    def __init__(
        self,
        message: str | None = None,
        data: Any | None = None,
        errors: list[Any] | None = None,
        status_code: int = status.HTTP_200_OK,
        **kwargs,
    ) -> None:
        content = {}
        if message:
            content["message"] = message
        if data:
            content["data"] = data
        if errors:
            content["errors"] = errors

        super().__init__(content=content, status_code=status_code, **kwargs)
