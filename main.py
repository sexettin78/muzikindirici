os.system("pip install youtube-dl")
print("Linki yapıştırın")
link = input ("")
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
