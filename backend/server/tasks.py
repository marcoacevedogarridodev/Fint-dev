import requests
from datetime import datetime
from celery import shared_task
import sqlite3

@shared_task
def fetch_mindicador_data():
    try:
        response = requests.get('https://mindicador.cl/api/')
        response.raise_for_status()
        data = response.json()
        
        indicadores = {
            'uf': data.get('uf', {}).get('valor'),
            'dolar': data.get('dolar', {}).get('valor'),
            'dolar_intercambio': data.get('dolar_intercambio', {}).get('valor'),
            'euro': data.get('euro', {}).get('valor'),
            'ipc': data.get('ipc', {}).get('valor'),
            'utm': data.get('utm', {}).get('valor'),
            'ivp': data.get('ivp', {}).get('valor'),
            'imacec': data.get('imacec', {}).get('valor'),
            'tpm': data.get('tpm', {}).get('valor'),
            'libra_cobre': data.get('libra_cobre', {}).get('valor'),
            'tasa_desempleo': data.get('tasa_desempleo', {}).get('valor'),
            'bitcoin': data.get('bitcoin', {}).get('valor')
        }
        
        save_to_database(indicadores)
        
        return indicadores
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def save_to_database(indicadores):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_indicador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uf REAL,
            dolar REAL,
            dolar_intercambio REAL,
            euro REAL,
            ipc REAL,
            utm REAL,
            ivp REAL,
            imacec REAL,
            tpm REAL,
            libra_cobre REAL,
            tasa_desempleo REAL,
            bitcoin REAL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        INSERT INTO server_indicador (
            uf, dolar, dolar_intercambio, euro, ipc, utm, ivp, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        indicadores.get('uf'),
        indicadores.get('dolar'),
        indicadores.get('dolar_intercambio'),
        indicadores.get('euro'),
        indicadores.get('ipc'),
        indicadores.get('utm'),
        indicadores.get('ivp'),
        indicadores.get('imacec'),
        indicadores.get('tpm'),
        indicadores.get('libra_cobre'),
        indicadores.get('tasa_desempleo'),
        indicadores.get('bitcoin')
    ))
    
    conn.commit()
    conn.close()
