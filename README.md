# SaludOcup – Pausas activas controladas por API & Webhooks

Este proyecto es un **visor multimedia automatizado** destinado a correr en múltiples equipos (PCs Windows) y mostrar contenido tipo:

- 🎥 Videos (YouTube, Vimeo, etc.)
- 🖼 Imágenes
- 📣 Mensajes o anuncios web embebidos
- ⏱ Con duración controlada remotamente por API

El sistema se ejecuta en segundo plano y **solo abre la ventana WebView cuando la API activamente envía un anuncio**, respetando:

- Estado (activo o inactivo)
- URL a mostrar
- Tiempo exacto de visualización (segundos o minutos)
- Control remoto del cierre del visor

Además, cada evento clave se envía a un **Webhook**, permitiendo que otro aplicativo recepcione y audite:

- ✅ Anuncios mostrados correctamente
- ⚠️ Anuncios terminados con errores
- 🏁 Finalización de visualización
- 👤 Usuario/Dispositivo donde fue ejecutado

---

## 🏗️ Estructura del proyecto

SaludOcup-Web-Version/
│── main.py -> Script principal
│── fechData.py -> Consulta API y validación del anuncio
│── .env -> Variables de entorno
│── user/getuser.py -> Obtiene nombre de usuario/ID de dispositivo
│── Events/successData.py -> Envía webhook de eventos exitosos
│── Events/errorData.py -> Envía webhook de errores
│── requirements.txt -> Dependencias
│── README.md -> Documentación del proyecto