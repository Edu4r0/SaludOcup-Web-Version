import requests
from Events.errorData import ErrorUrl
from user.getuser import getuser
from dotenv import load_dotenv
import os

load_dotenv()
URL_API = os.getenv("URLAPI")


def DataUrl():
    user = getuser()

    try:
        if not URL_API:
            raise Exception("No se encontró URLAPI en el .env")

        print("Consultando API:", URL_API)  # DEBUG

        # Petición a la API
        response = requests.get(URL_API, timeout=8)
        print("Status code:", response.status_code)  # DEBUG
        print("Respuesta cruda:", response.text)      # DEBUG

        if response.status_code >= 400:
            raise Exception(f"Error HTTP {response.status_code}: {response.text}")

        # Convertir a JSON
        try:
            data = response.json()
        except Exception as e:
            raise Exception(f"La API no devolvió JSON válido: {response.text}")

        print("JSON decodificado:", data)  # DEBUG

        # VALIDAR CAMPOS EXACTOS DEL JSON DE MOCKI
        run = data.get("run", False)
        url = data.get("url", None)
        time_seconds = data.get("time", None)

        # Si run=False, no hay anuncio
        if run is False:
            return None

        # Validar campos obligatorios
        if not url:
            raise Exception("Falta 'url' en la respuesta de la API")

        if not time_seconds:
            raise Exception("Falta 'time' en la respuesta de la API")

        return {
            "status": True,
            "url": url,
            "time": time_seconds
        }

    except Exception as error:
        ErrorUrl(user, str(error))
        return None
