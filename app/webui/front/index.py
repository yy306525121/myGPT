import random
import time

import gradio as gr

from app.models.models import get_model


def generate(content, history):
    message = []

    # 适配gradio的history和chatglm的history
    for idx, (user_msg, model_msg) in enumerate(history):
        if idx == len(history) - 1 and not model_msg:
            message.append({'role': 'user', 'content': user_msg})
            break
        if user_msg:
            message.append({'role': 'user', 'content': user_msg})
        if model_msg:
            message.append({'role': 'assistant', 'content': model_msg})

    client = get_model('chatglm3-6b', user_name='yangzy')
    for response, _ in client.chat_stream(content, message):
        yield response


def ui():
    demo = gr.ChatInterface(
        generate,
        chatbot=gr.Chatbot(height=300),
        title='知识库集成系统',
        description='询问关于知识库的问题',
        theme='soft',
        examples=['北京到上海最快的交通方式', '中国的首都是哪里?'],
        cache_examples=False,
        retry_btn=None,
        undo_btn='回撤',
        clear_btn='清空聊天记录')

    return demo
