import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_TOKEN = os.getenv("API_TOKEN", "")
    CHAT_ID = os.getenv("CHAT_ID", "")


settings = Settings()

