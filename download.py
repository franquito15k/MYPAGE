from flask import Flask, render_template, request, send_file, jsonify
from yt_dlp import YoutubeDL
import os
import json

app = Flask(__name__)

# Define la carpeta de descargas relativa al directorio actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'downloads')

# Crea la carpeta de descargas si no existe
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Funciones para manejar el archivo JSON
def cargar_json():
    json_path = os.path.join(BASE_DIR, 'data', 'global.json')
    if not os.path.exists(json_path):
        # Si el archivo no existe, lo crea con una estructura inicial
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, 'w') as json_file:
            json.dump({"global_download": 0}, json_file, indent=4)
    with open(json_path, 'r') as json_file:
        return json.load(json_file)

def guardar_json(data):
    json_path = os.path.join(BASE_DIR, 'data', 'global.json')
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Función para descargar el video
def download_video(url):
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'format': 'best',
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No se proporcionó una URL"}), 400

    try:
        # Descargar el video
        filename = download_video(url)

        # Incrementar el contador de descargas
        data_json = cargar_json()
        data_json['global_download'] += 1
        guardar_json(data_json)

        # Enviar el archivo al cliente
        return send_file(filename, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rutas para el redireccionamiento
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
