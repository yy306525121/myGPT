from typing import Optional, Union

from pydantic import BaseModel


class Response(BaseModel):
    success: bool = True
    message: Optional[str] = None
    data: Optional[Union[dict, list]] = {}
