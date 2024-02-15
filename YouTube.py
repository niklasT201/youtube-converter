from pytube import YouTube

def Download(link, destination):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=destination)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

if __name__ == "__main__":
    destination = r"C:\Users\snikl\Downloads\Playlist"
    link = input("Enter the YouTube video URL: ")
    Download(link, destination)
