import pyperclip
import time
import os
from plyer import notification
import yt_dlp

def download_video(link):
    # 1. Create a specific folder for Videos on Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    video_folder = os.path.join(desktop, "My_Videos")
    
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
        print(f"📁 Created new folder: {video_folder}")
    
    # 2. Set options to download Video in MP4 format
    ydl_opts = {
        'format': 'best[ext=mp4]/best', 
        'outtmpl': f'{video_folder}/%(title)s.%(ext)s',
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

print("🎬 Video Automation is active! Waiting for a link...")

last_link = ""

while True:
    current_link = pyperclip.paste().strip()

    if current_link != last_link and ("youtube.com" in current_link or "youtu.be" in current_link):
        print(f"🎥 Video Link Detected: {current_link}")
        
        notification.notify(
            title="Video Found!",
            message="Downloading MP4 to 'My_Videos' folder...",
            timeout=5
        )
        
        try:
            download_video(current_link)
            print("✨ Success! Check the 'My_Videos' folder on your Desktop.")
        except Exception as e:
            print(f"❌ Error: {e}")

        last_link = current_link

    time.sleep(2)