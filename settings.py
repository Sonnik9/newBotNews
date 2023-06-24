import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_TOKEN = os.getenv("API_TOKEN", "")
    CHAT_ID = os.getenv("CHAT_ID", "")
    # API_TOKEN = '5826732776:AAHWGm-qmTINd9rTJ7CGtFbDLlRIZKSkKUU'
    # CHAT_ID = '-1001579866760'

settings = Settings()

