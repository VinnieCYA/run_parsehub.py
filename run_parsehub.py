import requests

# API Key y Project Token
API_KEY = "tmbS9BqJvSuv"
PROJECT_TOKEN = "taVAbYJYjNUs"

# URL para ejecutar el scraper
run_url = f"https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/run"

# Petición para ejecutar el scraper
response = requests.post(run_url, data={"api_key": API_KEY})

# Verificar la respuesta
if response.status_code == 200:
    print("Scraper ejecutado correctamente")
else:
    print("Error al ejecutar el scraper:", response.text)
