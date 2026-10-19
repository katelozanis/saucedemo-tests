import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/").rstrip("/") + "/"
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
