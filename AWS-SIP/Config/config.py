import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path=".env")

class Config:
    BASE_URL = os.getenv("BASE_URL")
    
