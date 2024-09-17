from flask import Flask, render_template, request, send_file, jsonify
from yt_dlp import YoutubeDL
import os
import json

app = Flask(__name__)

#ruta temporal para enviar el video
DOWNLOAD_FOLDER = '/downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# script propio para descargar el video
def download_video(url):
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'format': 'best',
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename

# rutas para el redireccionamiento
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')
# rutas para el redireccionamiento


# url que recibe e envia solicitud, que es el videoda
@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No se proporcionó una URL"}), 400

    try:
        filename = download_video(url)
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#seccion  para actualziar el json
def cargar_json():
    with open('data/global.json', 'r') as json_file:#r es de read o lectura como en c
        return json.load(json_file)

def guardar_json(data):
    with open('data/global.json', 'w') as json_file: #w es de write o escritura como en c
        json.dump(data, json_file, indent=4)

@app.route('/sumar_descarga', methods=['POST'])
def sumar_descarga():
    data = cargar_json()
    
    data['global_download'] += 1 #incremento mi var de descargas
    
    guardar_json(data)
    
    return jsonify({"message": "Descarga sumada exitosamente!"})
#seccion  para actualziar el json


if __name__ == '__main__':
    app.run(debug=True)
