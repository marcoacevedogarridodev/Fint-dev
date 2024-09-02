import requests
from datetime import datetime
from .models import Indicador  
from celery import shared_task

@shared_task
def fetch_mindicador_data():
    try:
        response = requests.get('https://mindicador.cl/api/uf')
        response.raise_for_status() 
        data = response.json()
        print(data) 
        return data
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
