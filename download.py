from flask import Flask, render_template, request, send_file, jsonify
from yt_dlp import YoutubeDL #libreria para el funcionamiento de la descarga de videos
import os
import json
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'inter_bd'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)


# cambio la carpeta de descargas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'downloads')

# creo la carpeta de descargas si no existe
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# funcion para manejar el archivo JSON
def cargar_json():
    json_path = os.path.join(BASE_DIR, 'data', 'global.json')
    if not os.path.exists(json_path):
        #si la carpeta data no existe se crea ademas del json, evitar conflictos de descarga
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, 'w') as json_file:
            json.dump({"global_download": 0}, json_file, indent=4)
    with open(json_path, 'r') as json_file:
        return json.load(json_file)

def guardar_json(data):
    json_path = os.path.join(BASE_DIR, 'data', 'global.json')
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# funcion para descargar el video
def download_video(url):
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'format': 'best',
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename
    
def insertar_descarga(nombre_video):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO descargas_videos (nombre_video) VALUES (%s)", (nombre_video,))
    conn.commit()
    cursor.close()
    conn.close()

def incrementar_descarga(nombre_video):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE descargas_videos SET cantidades = cantidades + 1 WHERE nombre_video = %s", (nombre_video,))
    conn.commit()
    cursor.close()
    conn.close()

#aca recibe la url enviada por el usuario en donde se procede a descargar el video e enviar al usuario
@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No se proporcionó una URL"}), 400

    try:
        # descarga el video
        filename = download_video(url)
        nombre_video = os.path.basename(filename)

        # insertar o incrementar el contador de descarga
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM descargas_videos WHERE nombre_video = %s", (nombre_video,))
        result = cursor.fetchone()
        if result:
            incrementar_descarga(nombre_video)
        else:
            insertar_descarga(nombre_video)
        cursor.close()
        conn.close()

        # envia el archivo al usuario
        return send_file(filename, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ruta para el redireccionamiento del html
@app.route('/')
def index():
    return render_template('index.php')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
