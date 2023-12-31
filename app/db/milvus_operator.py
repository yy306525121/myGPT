import os
from typing import List

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Milvus


class MilvusOperator(object):
    def __init__(self, host: str = 'localhost', port: str = '19530', embedding_model_path: str = None):
        self._embedding = HuggingFaceEmbeddings(model_name=embedding_model_path,
                                                model_kwargs={'device': 'cpu'})
        self._connection = Milvus.from_documents(documents=[], embedding=self._embedding,
                                                 connection_args={'host': host, 'port': port, 'user': 'minioadmin',
                                                                  'password': 'minioadmin'})

    def add_documents(self, document_list: List[Document]):
        if document_list:
            self._connection.add_documents(document_list)

    def search(self, content: str = None) -> List[Document]:
        if content:
            return self._connection.similarity_search(query=content)
        return []

    def as_retriever(self):
        return self._connection.as_retriever(search_type='mmr', search_kwargs={'k': 4})
