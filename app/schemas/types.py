from enum import Enum


class ModelType(Enum):
    Unknown = 'unknown'
    ChatGLM = 'ChatGLM'

    @classmethod
    def get_type(cls, model_name: str):
        model_type = None
        model_name_lower = model_name.lower()
        if 'chatglm' in model_name_lower:
            model_type = ModelType.ChatGLM
        return model_type
