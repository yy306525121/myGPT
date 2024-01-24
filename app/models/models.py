import logging
from functools import singledispatch, lru_cache

from app.models import BaseModel
from app.schemas import ModelType

_models: dict = {}


def get_model(
        model_name,
        temperature=None,
        top_p=None,
        system_prompt=None,
        user_name=''
) -> BaseModel:
    msg = f'模型设置为了：{model_name}'
    model_type = ModelType.get_type(model_name)

    if model_type in _models.keys():
        return _models[model_type]

    model = None
    try:
        if model_type == ModelType.ChatGLM:
            logging.info(f'正在加载ChatGLM模型：{model_name}')
            from .ChatGLM import ChatGLMModel
            model = ChatGLMModel(model_name, user_name=user_name)
        else:
            raise NotImplementedError('模型类型不支持')
    except Exception as e:
        import traceback
        logging.error(f'发生错误：{e}')

    _models[model_type] = model
    return model
