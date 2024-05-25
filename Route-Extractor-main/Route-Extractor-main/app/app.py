import requests
from bs4 import BeautifulSoup
from flask import Flask, request
from mongo.mongo import insert

app = Flask(__name__)

def extraer_rutas(url):
    # Realizar la solicitud HTTP a la URL
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el HTML utilizando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar todas las etiquetas 'a' en el HTML
        enlaces = soup.find_all('a')
        
        # Extraer las rutas de los enlaces
        rutas = [enlace.get('href') for enlace in enlaces]
        
        # Filtrar las rutas que no comienzan con 'http' o 'https' (pueden ser relativas)
        rutas = [ruta for ruta in rutas if ruta.startswith('http') or ruta.startswith('https')]
        
        return rutas
    else:
        # Si la solicitud no fue exitosa, imprimir un mensaje de error
        print("Error al obtener la página:", response.status_code)
        return []

def insertar_rutas_en_base_de_datos(rutas):
    for ruta in rutas:
        insert(ruta, request.remote_addr)
    print("Rutas insertadas en la base de datos")

if __name__ == '__main__':
    app.run(debug=True)