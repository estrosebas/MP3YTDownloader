import yt_dlp
import os

def descargar_audio(url, output_path='.'):
    try:
        # Opciones para la descarga
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'geo_bypass': True,
            'noplaylist': True,
            'quiet': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Descargando audio...")
            ydl.extract_info(url, download=True)
            print("¡Descarga completada!")

    except Exception as e:
        print(f"Error al descargar el audio: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube: ")
    output_dir = input("Ingresa la carpeta de destino (deja en blanco para usar la carpeta actual): ")

    if not output_dir:
        output_dir = "."

    descargar_audio(url, output_dir)
