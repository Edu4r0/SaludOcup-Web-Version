import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK_URL = os.getenv("URL_WEBHOOK")

def ErrorUrl(user, error):
    if not WEBHOOK_URL:
        print("ERROR: No se encontró URL_WEBHOOK en el .env")
        return

    data = {
        "name": user,
        "date": datetime.now().isoformat(),
        "error": str(error)
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)
        print("Webhook enviado. Código:", response.status_code)
    except Exception as e:
        print("Error enviando webhook:", str(e))
