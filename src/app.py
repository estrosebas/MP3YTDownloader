from flask import Flask, request, render_template, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)
UPLOAD_FOLDER = "cookies"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    output_dir = request.form["output_dir"] or "downloads"
    os.makedirs(output_dir, exist_ok=True)

    # Manejar la carga del archivo de cookies
    cookie_path = None
    if "cookies" in request.files:
        file = request.files["cookies"]
        if file.filename:
            cookie_path = os.path.join(UPLOAD_FOLDER, "cookies.txt")
            file.save(cookie_path)

    # Opciones para yt-dlp
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    # Si hay cookies, agrégalas a yt-dlp
    if cookie_path:
        ydl_opts["cookies"] = cookie_path

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Download complete!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
