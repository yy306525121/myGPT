from app import settings
from app.schemas import ModelType


class BaseModel:
    def __init__(self,
                 model_name: str,
                 system_prompt=settings.INITIAL_SYSTEM_PROMPT,
                 temperature=1.0,
                 top_p=1.0,
                 max_generation_token=None,
                 user: str = None) -> None:
        self.all_token_counts = []
        self.model_name = model_name
        self.model_type = ModelType.get_type(self.model_name)
        self.system_prompt = system_prompt
        self.history_redis_key = 'history_{user}'.format(user=user)
        self.user = user
        self.default_temperature = temperature
        self.default_top_p = top_p
        self.default_max_generation_token = max_generation_token
        self.load()

    def load(self):
        pass

    def chat(self, content: str, history) -> str:
        """
        聊天(带历史记录）
        @rtype: Tuple
        """
        pass

    def chat_stream(self, content: str, history):
        pass
