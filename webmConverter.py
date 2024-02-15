import subprocess

def convert_webm_to_mp3(webm_file_path, mp3_file_path):
    command = 'ffmpeg -i "{}" -vn -ar 44100 -ac 2 -b:a 192k "{}"'.format(webm_file_path, mp3_file_path)
    subprocess.call(command, shell=True)

webm_file = r"C:\Users\snikl\Downloads\Playlist\Auf Achse.webm"
mp3_file = r"C:\Users\snikl\Downloads\Songs\Auf Achse.mp3"

convert_webm_to_mp3(webm_file, mp3_file)
