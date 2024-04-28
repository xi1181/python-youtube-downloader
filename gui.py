import tkinter as tk
from tkinter import filedialog
from check_youtube_url import is_valid_url
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_video():
    url = website_entry.get()
    save_path = folderpath.get()
    if not save_path:
        messagebox.showerror("Error", "Please select a folder to save the video")
        return
    if not is_valid_url(url):
        messagebox.showerror("Error", "Invalid Youtube URL")
        return
    try:
        yt = YouTube(url)
        # print(yt.streams)

        if boomp3.get():
            audio_stream = yt.streams.filter(only_audio = True).first()

            if audio_stream:
                out_file = audio_stream.download(save_path)
                base, ext = os.path.splitext(out_file)
                new_file =  base + ".mp3"
                audio_clip = AudioFileClip(out_file)
                audio_clip.write_audiofile(new_file)
                audio_clip.close()
                os.remove(out_file)

        if boomp4.get():
            video_stream = yt.streams.filter(progressive = True,
                                            file_extension = "mp4").order_by("resolution").desc().first()
            if video_stream:
                video_stream.download(save_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to downlad video:{e}")
    else:
        messagebox.showinfo("Sucess!",  f"Video/Audio has been downloaded to {save_path}")
        
def select_folder():
    fs = filedialog.askdirectory(initialdir=os.getcwd())
    folderpath.set(fs)

window = tk.Tk()
window.title("Youtube Video Downloader")
tk.Label(window,text="Youtube URL:").pack()


website_entry = tk.Entry(window, width=50)
website_entry.pack(padx=20)

boomp4 = tk.BooleanVar()
check_buttonmp4 = tk.Checkbutton(window, text="Download MP4", variable=boomp4)
check_buttonmp4.pack()
boomp3 = tk.BooleanVar()
check_buttonmp3 = tk.Checkbutton(window, text="Download MP3", variable=boomp3)
check_buttonmp3.pack()

folder_button =  tk.Button(window, text="Choose Folder" ,command=select_folder)
folder_button.pack()

folderpath = tk.StringVar(value = os.getcwd())
folderpath_entry = tk.Entry(window, textvariable=folderpath, width=50, state="disabled")
folderpath_entry.pack(padx=20)

download_button = tk.Button(window, text="Download", command = download_video)
download_button.pack()


window.mainloop()