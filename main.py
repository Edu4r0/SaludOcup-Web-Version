import time
import threading
import requests
import webview
from datetime import datetime
from dotenv import load_dotenv
import os
from user.getuser import getuser
from Events.successData import SuccessUrl
from Events.errorData import ErrorUrl

load_dotenv()

URL_API = os.getenv("URLAPI")

# Horarios (24H)
SCHEDULES = ["08:50", "11:25"]  # 10:30 AM y 2:30 PM

# Para evitar repetir anuncios el mismo día
shown_today = set()


def get_api_data():
    """Consulta API y retorna dict { status, url, time }"""
    print(f"Consultando API: {URL_API}")

    try:
        response = requests.get(URL_API, timeout=8)
        print("Status code:", response.status_code)
        print("Respuesta cruda:", response.text)

        data = response.json()
        print("JSON decodificado:", data)

        return {
            "status": data.get("status", "inactive"),
            "url": data.get("url"),
            "time": data.get("time", 10)
        }

    except Exception:
        return None


def show_webview(url, duration):
    """Muestra anuncio X segundos y lo cierra"""

    print(f"==> ABRIENDO WEBVIEW: {url}")

    window = webview.create_window(
        "SOP",
        url,
        fullscreen=True,
        on_top=True
    )

    # Thread que cierra la ventana automáticamente
    def auto_close():
        time.sleep(duration)
        print("==> CERRANDO WEBVIEW")
        window.destroy()

    threading.Thread(target=auto_close, daemon=True).start()

    # Inicia ventana (bloquea hasta cerrar)
    webview.start()


def listener_loop():
    user = getuser()
    print("Sistema iniciado. Esperando horarios programados...")

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        today = now.strftime("%Y-%m-%d")

        # Verifica si estamos en un horario fijado
        if current_time in SCHEDULES:

            # Evitar ejecutar más de una vez ese horario hoy
            unique_id = f"{today}_{current_time}"

            if unique_id not in shown_today:
                print(f"\n EJECUTANDO ANUNCIO PROGRAMADO A LAS {current_time}")

                data = get_api_data()

                if not data:
                    ErrorUrl(user, "Error obteniendo datos de la API")
                    shown_today.add(unique_id)
                    continue

                status = data["status"]
                url = data["url"]
                seconds = data["time"]

                if status == "active" and url:
                    # Webhook: anuncio detectado
                    SuccessUrl(user, f"Anuncio programado detectado: {url}")

                    show_webview(url, seconds)

                    # Webhook: anuncio terminado
                    SuccessUrl(user, f"Anuncio mostrado correctamente ({seconds}s)")

                    print("==> ANUNCIO TERMINADO")

                else:
                    ErrorUrl(user, "Horario llegó, pero API no entregó anuncio")

                # Registrar que ya se ejecutó este horario hoy
                shown_today.add(unique_id)

            else:
                print(f"Ya se ejecutó el anuncio de las {current_time} hoy.")

        # Cada 20s revisa hora nuevamente (suficiente)
        time.sleep(20)


if __name__ == "__main__":
    listener_loop()
