from backend.clients.clients.BaseClient import BaseClient
import os
import openai

class ChatGPTClient(BaseClient):
    pass



    def fetch():
        openai.organization = "org-b0lHkvWyudHGonqMoxesR48K"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.Model.list()