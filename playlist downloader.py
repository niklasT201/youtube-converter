from pytube import Playlist, YouTube
import os

def download_playlist(playlist_link, destination):
    skipped_songs = []
    try:
        playlist = Playlist(playlist_link)
        for video in playlist.video_urls:
            print(f"Downloading {video}")
            youtubeObject = YouTube(video)
            try:
                stream = youtubeObject.streams.get_highest_resolution()
                if stream:
                    stream.download(output_path=destination)
                else:
                    print(f"No stream available for {youtubeObject.title}. Skipping...")
                    skipped_songs.append(youtubeObject.title)
            except Exception as e:
                print(f"Skipped {youtubeObject.title} due to error:", e)
                skipped_songs.append(youtubeObject.title)
        print("Download is completed successfully")
    except Exception as e:
        print("An error has occurred:", e)
    finally:
        if skipped_songs:
            print("\nSkipped songs:")
            for song in skipped_songs:
                print(song)

if __name__ == "__main__":
    playlist_link = input("Enter the YouTube playlist URL: ")
    destination = r'C:\Users\snikl\Downloads\Playlist'  # Change destination directory here
    if not os.path.exists(destination):
        os.makedirs(destination)
    download_playlist(playlist_link, destination)
