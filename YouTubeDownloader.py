import yt_dlp # pip install -U yt-dlp

# тут ссылка на видео которое ты хоч скачать
url = "https://www.youtube.com/watch?v=NLBsQYLp2uI"

# тут настройки для видео
ydl_opts = {
    "format": "bestvideo",
    "outtmpl": "%(title)s_video.%(ext)s",
}

# тут оно качает
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# запуск 1. смд, 2. где файл .py ты копируешь путь, 3. пишешь в смд cd (путь без скобок) 4. пишешь python need.py (или как ты назвал файл) если не запускается, пиши python3 need.py 