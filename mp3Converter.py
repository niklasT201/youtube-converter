import os
from moviepy.editor import *

def convert_mp4_to_mp3(mp4_folder_path, mp3_folder_path):
    try:
        for file_name in os.listdir(mp4_folder_path):
            if file_name.endswith(".mp4"):
                mp4_file_path = os.path.join(mp4_folder_path, file_name)
                mp3_file_path = os.path.join(mp3_folder_path, os.path.splitext(file_name)[0] + ".mp3")
                
                # Load the mp4 file
                video = VideoFileClip(mp4_file_path)

                # Extract audio from video and save as mp3
                video.audio.write_audiofile(mp3_file_path)

                print(f"Converted {mp4_file_path} to {mp3_file_path}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    mp4_folder_path = r"C:\Users\snikl\Downloads\Playlist"
    mp3_folder_path = r"C:\Users\snikl\Downloads\Songs"

    if not os.path.exists(mp3_folder_path):
        os.makedirs(mp3_folder_path)

    convert_mp4_to_mp3(mp4_folder_path, mp3_folder_path)
