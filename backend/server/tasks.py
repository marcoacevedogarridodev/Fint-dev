import requests
from datetime import datetime
from .models import Indicador  
from celery import shared_task
import sqlite3

@shared_task
def fetch_mindicador_data():
    try:
        response = requests.get('https://mindicador.cl/api/uf/')
        response.raise_for_status() 
        data = response.json()
        
        if data['serie']:
            primer_valor = data['serie'][0]['valor']
            save_to_database(primer_valor)
            return primer_valor
        else:
            print("No data available.")
            return None
     
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def save_to_database(valor):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_indicador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uf INTEGER,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('INSERT INTO server_indicador (uf) VALUES (?)', (valor,))
    
    conn.commit()
    conn.close()

fetch_mindicador_data()