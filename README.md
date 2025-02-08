# YouTube Audio Downloader

Este script permite descargar el audio de un video de YouTube en formato MP3 utilizando la biblioteca `yt_dlp`.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalados los siguientes requisitos:

- Python 3
- `yt-dlp`
- `ffmpeg`

### Instalación de dependencias

Ejecuta los siguientes comandos para instalar las dependencias necesarias:

```sh
pip install yt-dlp
```

Además, debes tener `ffmpeg` instalado en tu sistema:

- **Windows:** Descarga `ffmpeg` desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) y agrégalo al `PATH`.
- **Linux/macOS:** Instálalo con:
  ```sh
  sudo apt install ffmpeg  # Ubuntu/Debian
  brew install ffmpeg      # macOS
  ```

## Uso

Ejecuta el script con el siguiente comando:

```sh
python script.py
```

El script solicitará:

1. La URL del video de YouTube.
2. La carpeta de destino (opcional, por defecto usa la carpeta actual).

Ejemplo de ejecución:

```sh
Ingresa la URL del video de YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Ingresa la carpeta de destino (deja en blanco para usar la carpeta actual):
```

## Opciones y Características

- Descarga el mejor audio disponible en formato MP3.
- Utiliza `ffmpeg` para extraer el audio y convertirlo a 192 kbps.
- Permite elegir la carpeta de destino para el archivo descargado.
- Evita descargar listas de reproducción (solo descarga un video a la vez).

## Notas

- Si `yt-dlp` deja de funcionar, actualízalo con:
  ```sh
  pip install --upgrade yt-dlp
  ```
- Asegúrate de tener `ffmpeg` correctamente configurado en tu sistema.

## Licencia

Este proyecto es de uso libre. ¡Disfruta descargando tu música favorita! 🎵
