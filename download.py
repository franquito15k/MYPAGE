from flask import Flask, request, jsonify, send_file
import yt_dlp
import os

app = Flask(__name__)

# Ruta de la carpeta de Descargas en Windows
DOWNLOADS_FOLDER = os.path.expanduser('~/Downloads')

# Función para descargar video usando yt-dlp
def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'noplaylist': True,
        'outtmpl': os.path.join(DOWNLOADS_FOLDER, 'downloaded_video.%(ext)s')  # Ruta completa del archivo
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url)
            filename = ydl.prepare_filename(result)
            if os.path.exists(filename):  # Verifica si el archivo fue descargado correctamente
                return filename
            else:
                print("El archivo no fue encontrado.")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Ruta que maneja la descarga del video
@app.route('/download_video', methods=['POST'])
def download_video_route():
    url = request.form.get('url')  # Obtén la URL del formulario
    if not url:
        return jsonify({'error': 'No se proporcionó una URL'}), 400

    # Descargar el video
    filename = download_video(url)
    if filename:
        try:
            # Enviar el archivo descargado al cliente
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return jsonify({'error': f'No se pudo enviar el archivo: {e}'}), 500
    else:
        return jsonify({'error': 'Ocurrió un error al descargar el video'}), 500

if __name__ == "__main__":
    app.run(debug=True)
