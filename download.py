from flask import Flask, render_template, request, send_file, jsonify, redirect,url_for
from yt_dlp import YoutubeDL
import os
import json
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'inter_bd'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexión a la base de datos establecida correctamente.")
            return conn
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

# Cambio de la carpeta de descargas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'downloads')

# Creo la carpeta de descargas si no existe
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Función para manejar el archivo JSON
def cargar_json():
    json_path = os.path.join(BASE_DIR, 'data', 'global.json')
    if not os.path.exists(json_path):
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

def insertar_descarga(nombre_video):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            print(f"Intentando insertar descarga para el video: {nombre_video}")
            cursor.execute("INSERT INTO descargas_videos (nombre_video) VALUES (%s)", (nombre_video,))
            conn.commit()
            print(f"Descarga insertada correctamente para el video: {nombre_video}")
        except Error as e:
            print(f"Error al insertar descarga: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

def incrementar_descarga(nombre_video):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            print(f"Intentando incrementar descarga para el video: {nombre_video}")
            cursor.execute("UPDATE descargas_videos SET cantidades = cantidades + 1 WHERE nombre_video = %s", (nombre_video,))
            conn.commit()
            print(f"Descarga incrementada correctamente para el video: {nombre_video}")
        except Error as e:
            print(f"Error al incrementar descarga: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

# Recibe la URL enviada por el usuario y procede a descargar el video
@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No se proporcionó una URL"}), 400

    try:
        # Descarga el video
        filename = download_video(url)
        nombre_video = os.path.basename(filename)

        # Insertar o incrementar el contador de descarga
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM descargas_videos WHERE nombre_video = %s", (nombre_video,))
            result = cursor.fetchone()
            if result:
                incrementar_descarga(nombre_video)
            else:
                insertar_descarga(nombre_video)
            cursor.close()
            conn.close()
        
        # Enviar el archivo descargado al usuario
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)
        return send_file(filepath, as_attachment=True)

    except Exception as e:
        print(f"Error en el proceso de descarga: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    conn = get_db_connection()
    nombre_usuario = None
    id_usuario = None

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM sesiones ORDER BY last_activity DESC LIMIT 1")
            result = cursor.fetchone()
            if result:
                nombre_usuario = result[0]
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error al obtener el nombre del usuario: {e}")

    print(f"Nombre del usuario: {nombre_usuario}")  # Agrega esta línea para depurar

    return render_template('index.php', nombre_usuario=nombre_usuario)

@app.route('/logout', methods=['POST'])
def logout():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Obtener el nombre de usuario de la sesión activa
            cursor.execute("SELECT username FROM sesiones ORDER BY last_activity DESC LIMIT 1")
            result = cursor.fetchone()
            if result:
                nombre_usuario = result[0]
                # Borrar la sesión del usuario actual
                cursor.execute("DELETE FROM sesiones WHERE username = %s", (nombre_usuario,))
                conn.commit()
                print(f"Sesión de {nombre_usuario} cerrada correctamente.")
            else:
                print("No hay sesión activa.")
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error al cerrar sesión: {e}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)