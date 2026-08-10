import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "AI_CREATIVE_LAB")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")