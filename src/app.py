import os
from flask import Flask, request, render_template
from downloader import download_audio

app = Flask(__name__)

UPLOAD_FOLDER = 'cookies'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    output_dir = request.form.get('output_dir', '')

    # Guardar el archivo de cookies si se sube
    cookie_file_path = None
    if 'cookies' in request.files:
        file = request.files['cookies']
        if file.filename:
            cookie_file_path = os.path.join(UPLOAD_FOLDER, 'cookies.txt')
            file.save(cookie_file_path)

    result = download_audio(url, output_dir, cookie_file_path)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, ssl_context=(
        '/etc/letsencrypt/live/radioaqp.serveirc.com/fullchain.pem',
        '/etc/letsencrypt/live/radioaqp.serveirc.com/privkey.pem'
    ))
