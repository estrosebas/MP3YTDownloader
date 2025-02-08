import yt_dlp
import re
import os

def sanitize_filename(title):
    # Elimina caracteres problemáticos
    return re.sub(r'[<>:"/\\|?*]', '', title).replace(' ', '_')

def download_audio(url, output_dir, cookie_file=None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    if cookie_file:
        ydl_opts['cookiefile'] = cookie_file

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        title = sanitize_filename(info_dict.get('title', 'audio'))
        ydl_opts['outtmpl'] = os.path.join(output_dir, f"{title}.%(ext)s")
        ydl.download([url])
    
    return title  # Retornar el nombre limpio del archivo

