from typing import List

from pydantic import BaseModel


class LoginReq(BaseModel):
    username: str
    password: str


class UserInfo(BaseModel):
    id: int
    username: str
    is_active: bool
    roles: str
