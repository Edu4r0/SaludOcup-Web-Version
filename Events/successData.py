import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
WEBHOOK_URL = os.getenv("URL_WEBHOOK")

def SuccessUrl(user, message="OK"):
    data = {
        "name": user,
        "date": datetime.now().isoformat(),
        "status": "success",
        "message": message
    }

    try:
        requests.post(WEBHOOK_URL, json=data, timeout=5)
    except:
        pass
