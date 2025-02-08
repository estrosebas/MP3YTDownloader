from flask import Flask, request, render_template
from downloader import download_audio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])'POST'])
def download():
    url = request.form['url']
    output_dir = request.form.get('output_dir', '')output_dir', '')
    result = download_audio(url, output_dir) download_audio(url, output_dir)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=(
        '/etc/letsencrypt/live/radioaqp.serveirc.com/fullchain.pem',n.pem',
        '/etc/letsencrypt/live/radioaqp.serveirc.com/privkey.pem'serveirc.com/privkey.pem'
    ))