import pyperclip
import time
import os
from plyer import notification
import yt_dlp

def download_audio(link):
    # 1. Create a specific folder for Audios on Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    audio_folder = os.path.join(desktop, "My_Audios")
    
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
        print(f"📁 Created new folder: {audio_folder}")

    # 2. Set options to download ONLY audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{audio_folder}/%(title)s.%(ext)s',
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

print("🎧 MP3/Audio Automation is active! Copy a link to start.")

last_link = ""

while True:
    current_link = pyperclip.paste().strip()

    if current_link != last_link and ("youtube.com" in current_link or "youtu.be" in current_link):
        print(f"🎵 Audio Link Detected: {current_link}")
        
        notification.notify(
            title="Audio Found!",
            message="Downloading music to 'My_Audios' folder...",
            timeout=5
        )
        
        try:
            download_audio(current_link)
            print("✨ Success! Check the 'My_Audios' folder on your Desktop.")
        except Exception as e:
            print(f"❌ Error: {e}")

        last_link = current_link

    time.sleep(2)