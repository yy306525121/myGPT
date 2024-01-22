from dotenv import load_dotenv

from app.core import settings


def load_env():
    if not load_dotenv(settings.CONFIG_PATH / '.env'):
        print("Could not load .env file or it is empty. Please check if it exists and is readable.")
        exit(1)