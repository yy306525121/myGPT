from pydantic import BaseModel


class Model(BaseModel):
    """模型数据"""
    id: int
    name: str
    status: str
    model_type: str
    model_name: str
    