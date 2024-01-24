import logging
import os.path
from typing import List, Tuple

from app.core import settings
from app.models import BaseModel
from app.utils import get_device


class ChatGLMModel(BaseModel):
    def __init__(self, model_name, user_name=""):
        self.model_name = model_name
        self.user = user_name
        self.tokenizer = None
        self.model = None
        super().__init__(model_name=model_name, user=user_name)

    def load(self):
        try:
            from transformers import AutoTokenizer, AutoModel

            model_path = settings.MODEL_PATH / self.model_name
            if not os.path.exists(model_path):
                model_path = f'THUDM/{self.model_name}'
            self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
            self.model = AutoModel.from_pretrained(model_path, trust_remote_code=True)

            device = get_device()
            if device == 'cuda':
                logging.info('CUDA is available, using CUDA')
                self.model = self.model.half().cuda()
            elif device == 'mps':
                logging.info('MPS is available, using MPS')
                self.model = self.model.to('mps')
            elif device == 'cpu':
                logging.info('CPU is available, using CPU')
                self.model = self.model.float()
            self.model = self.model.eval()
            return self.model
        except ModuleNotFoundError as e:
            logging.error(f'transformers包引入失败: {e}')

    def chat(self, content: str, history):
        response, history = self.model.chat(self.tokenizer, query=content, history=history)
        return response, history

    def chat_stream(self, content: str, history):
        return self.model.stream_chat(self.tokenizer, query=content, history=history)








