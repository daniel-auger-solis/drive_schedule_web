from __future__ import print_function
import streamlit as st
import datetime
import gspread
from google.oauth2.service_account import Credentials
import json
import base64

st.title("Registro automático de visitas")

# --- Código que se ejecuta automáticamente al entrar ---
try:
    # Leer credenciales desde Streamlit Secrets
    # En Secrets de Streamlit Cloud:
    # [google]
    # credentials_json = "TU_BASE64_DEL_JSON"
    credentials_b64 = st.secrets["google"]["credentials_json"]
    credentials_dict = json.loads(base64.b64decode(credentials_b64))

    # Alcances necesarios para Google Sheets y Drive
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
              "https://www.googleapis.com/auth/drive"]

    # Crear credenciales desde el JSON en memoria
    creds = Credentials.from_service_account_info(credentials_dict, scopes=SCOPES)

    # Conectar con Google Sheets
    client = gspread.authorize(creds)

    # ID de tu hoja de cálculo
    SPREADSHEET_ID = "1ZWqpLUSZ0QuHAJf4vb48JCP-kYSlXGz7BqMybk7KHgI"

    # Abrir la primera hoja
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1

    # Contar filas existentes
    values = sheet.get_all_values()
    if not values:
        next_action_number = 1
    else:
        last_row = values[-1]
        if last_row and last_row[0].startswith("Accion"):
            try:
                last_number = int(last_row[0].split()[1])
                next_action_number = last_number + 1
            except (IndexError, ValueError):
                next_action_number = len(values)
        else:
            next_action_number = len(values)

    accion = f"Accion {next_action_number}"
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sheet.append_row([accion, fecha])

    st.success(f"Registro agregado automáticamente: {accion} - {fecha}")

except Exception as e:
    st.error(f"Ocurrió un error al registrar la acción: {e}")
