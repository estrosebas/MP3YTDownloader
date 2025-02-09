# Flask API for YouTube Audio Downloader

This project is a Flask web application that allows users to download audio from YouTube videos. It utilizes the `yt_dlp` library for downloading and processing audio files.

## Project Structure

```
flask-api
├── src
│   ├── app.py          # Entry point of the Flask application
│   ├── downloader.py   # Contains the audio downloading logic
│   └── templates
│       └── index.html  # HTML template for the web interface
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```
## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python src/app.py
   ```

   The application will be accessible at `https://localhost:5020`.

## Usage Guidelines

1. Open your web browser and navigate to `https://localhost:5020`.
2. Enter the YouTube video URL in the provided form.
3. Specify the output directory for the downloaded audio (leave blank for the current directory).
4. Click the "Download" button to start the audio download.

## Note

Ensure that the SSL certificates (`fullchain.pem` and `privkey.pem`) are correctly placed in the `certs` directory for secure HTTPS connections.