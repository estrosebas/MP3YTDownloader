import os
from flask import Flask, request, render_template, send_file
from downloader import download_audio

app = Flask(__name__)

UPLOAD_FOLDER = 'cookies'
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    output_dir = DOWNLOAD_FOLDER  # Guardar siempre en la carpeta de descargas

    # Guardar el archivo de cookies si se sube
    cookie_file_path = None
    if 'cookies' in request.files:
        file = request.files['cookies']
        if file.filename:
            cookie_file_path = os.path.join(UPLOAD_FOLDER, 'cookies.txt')
            file.save(cookie_file_path)

    result = download_audio(url, output_dir, cookie_file_path)

    # Obtener el archivo descargado
    downloaded_files = os.listdir(output_dir)
    if not downloaded_files:
        return "Error: No se encontró el archivo descargado.", 500

    # Suponiendo que solo se descargó un archivo, obtén su nombre
    downloaded_file = os.path.join(output_dir, downloaded_files[0])

    # Enviar el archivo al usuario
    return send_file(downloaded_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, ssl_context=(
        '/etc/letsencrypt/live/radioaqp.serveirc.com/fullchain.pem',
        '/etc/letsencrypt/live/radioaqp.serveirc.com/privkey.pem'
    ))
