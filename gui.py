import tkinter as tk
from tkinter import filedialog
from check_youtube_url import is_valid_url
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = website_entry.get()
    save_path = folderpath.get()
    if not save_path:
        messagebox.showerror("Error", "Please select a folder to save the video")
        return
    if not is_valid_url(url):
        messagebox.showerror("Error", "Invalid Youtube URL")
        return
    yt = YouTube(url)
    print(yt.streams)
    
    
def select_folder():
    fs = filedialog.askdirectory()
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

folderpath = tk.StringVar()
folderpath_entry = tk.Entry(window, textvariable=folderpath, width=50)
folderpath_entry.pack(padx=20)

download_button = tk.Button(window, text="Download", command = download_video)
download_button.pack()


window.mainloop()