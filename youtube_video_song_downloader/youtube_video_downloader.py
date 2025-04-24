from tkinter import *
from tkinter import filedialog
import yt_dlp

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    video_or_song = radio_var.get()
    video_url = url_entry.get()
    save_path = path_label.cget("text")
    
    try:
        print("Downloading:", video_or_song)
        #If need the highest quality video we need to install FFmpeg as high quality video have seperate audio and video
        if video_or_song == "video":
            # Download both best video and best audio for video download
            ydl_opts = {
                'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save in the selected path
                # 'format': 'bestvideo+bestaudio/best',  # Highest video and audio quality
                'format': 'best',
                'merge_output_format': 'mp4',  # Merge video and audio into an mp4 container
            }
        
        elif video_or_song == "song":
            # Download the best audio stream and extract as MP3
            ydl_opts = {
                'outtmpl': save_path + '/%(title)s.%(ext)s',
                'format': 'bestaudio/best',  # Best audio quality
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',  # Convert to MP3 after downloading
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',  # Set MP3 quality (192 kbps or higher)
                }],
            }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])  # Download the video or audio

        print("Download completed:", video_or_song)

    except Exception as e:
        print("Download failed:", e)

# GUI
root = Tk()
root.title('YouTube Downloader')
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Title label
app_label = Label(root, text="YouTube Downloader", fg="blue", font=("Arial", 20))
canvas.create_window(200, 20, window=app_label)

# URL input
url_label = Label(root, text="Enter YouTube URL:")
url_entry = Entry(root, width=40)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# Radio buttons
radio_var = StringVar(value="video")
radio_button1 = Radiobutton(root, text="Download as Video (MP4)", variable=radio_var, value="video")
radio_button2 = Radiobutton(root, text="Download as Audio (MP3)", variable=radio_var, value="song")
canvas.create_window(200, 140, window=radio_button1)
canvas.create_window(200, 160, window=radio_button2)

# Path selection
path_label = Label(root, text="Select download folder")
path_button = Button(root, text="Browse", command=get_path)
canvas.create_window(200, 200, window=path_label)
canvas.create_window(200, 220, window=path_button)

# Download button
download_button = Button(root, text="Download", command=download_file)
canvas.create_window(200, 260, window=download_button)

root.mainloop()
