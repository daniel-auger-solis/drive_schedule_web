# Registro Automático de Visitas - Streamlit

Esta aplicación de **Streamlit** permite registrar automáticamente visitas en una hoja de Google Sheets. Cada vez que alguien abre la página, se agrega una nueva fila con la acción y la fecha/hora.

---

## Ejecutar código
Abrir el siguiente enlace para ejecutar el código: https://drive-schedule-web.onrender.com/

## 🚀 Requisitos

- Python 3.10+
- Streamlit
- gspread
- google-auth

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuración del JSON Secreto de Google

Para conectarse a Google Sheets se necesita un **JSON de credenciales** de Google Cloud.  

### Pasos:

1. Convierte tu archivo JSON a **Base64** (Windows PowerShell):

```powershell
[Convert]::ToBase64String([IO.File]::ReadAllBytes("geminiapi-470823-262f80dddb02.json")) | clip
```

Esto copiará el contenido Base64 al portapapeles.

2. Define los **Secrets** de Streamlit:

- Abre **Streamlit Cloud → Manage → Secrets** y agrega lo siguiente:

```toml
[google]
credentials_json = "PASTE_AQUI_TU_BASE64"
```

Reemplaza "PASTE_AQUI_TU_BASE64" por el contenido que copiaste en el paso anterior.

---

## ⚡ Uso Local

1. Ejecuta la app localmente:

```bash
streamlit run app.py
```
