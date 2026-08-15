import asyncio
import os
import re
from typing import Union
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from py_yt import VideosSearch, Playlist

DOWNLOAD_DIR = "downloads"

# yt-dlp options (Cookies support ke saath)
def get_ydl_opts(is_video=False):
    opts = {
        "format": "bestvideo+bestaudio/best" if is_video else "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
    }
    if os.path.exists("cookies.txt"):
        opts["cookiefile"] = "cookies.txt"
    return opts

async def download_song(link: str) -> str:
    # URL se video_id extract karna
    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.webm") # ya .mp3
    
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    # yt-dlp se direct download
    try:
        ydl_opts = get_ydl_opts(is_video=False)
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["outtmpl"] = file_path
        
        loop = asyncio.get_event_loop()
        def download():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        await loop.run_in_executor(None, download)
        
        if os.path.exists(file_path):
            return file_path
        return None
    except Exception as e:
        print(f"Download Error: {e}")
        return None

async def download_video(link: str) -> str:
    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp4")
    
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    try:
        ydl_opts = get_ydl_opts(is_video=True)
        ydl_opts["outtmpl"] = file_path
        
        loop = asyncio.get_event_loop()
        def download():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        await loop.run_in_executor(None, download)
        
        if os.path.exists(file_path):
            return file_path
        return None
    except Exception as e:
        print(f"Video Download Error: {e}")
        return None

# Baki class YouTubeAPI waise hi rehne dein, bas download_song aur download_video ko upar wale code se replace kar dein.
