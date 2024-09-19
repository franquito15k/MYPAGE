from flask import Flask, render_template, request, send_file, jsonify
from yt_dlp import YoutubeDL
from io import BytesIO
import json

app = Flask(__name__)

# Script propio para descargar el video en memoria
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
        'outtmpl': '-',  # Especifica que no se debe guardar en disco
    }
    
    buffer = BytesIO()  # Crea un buffer en memoria para almacenar el video

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)  # No descargues el archivo directamente
        ydl.download([url])
        buffer.write(ydl.sanitize_info(info)['url'].encode('utf-8'))  # Escribe los datos en el buffer

    buffer.seek(0)  # Reinicia el puntero del buffer
    return buffer, info['title']  # Devuelve el buffer y el título del video para usar como nombre de archivo

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

# URL que recibe y envía solicitud para descargar el video
@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No se proporcionó una URL"}), 400

    try:
        buffer, title = download_video(url)
        return send_file(buffer, as_attachment=True, download_name=f"{title}.mp4", mimetype='video/mp4')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Sección para actualizar el JSON
def cargar_json():
    with open('data/global.json', 'r') as json_file:
        return json.load(json_file)

def guardar_json(data):
    with open('data/global.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

@app.route('/sumar_descarga', methods=['POST'])
def sumar_descarga():
    data = cargar_json()
    
    data['global_download'] += 1  # Incrementa la variable de descargas
    
    guardar_json(data)
    
    return jsonify({"message": "Descarga sumada exitosamente!"})

if __name__ == '__main__':
    app.run(debug=True)
