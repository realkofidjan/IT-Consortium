import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class Config:
    BASE_URL = os.getenv("BASE_URL")
    
