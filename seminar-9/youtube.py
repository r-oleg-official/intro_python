from pytube import YouTube 
from pytube.cli import on_progress


def list_res(url) -> str:
    yt = YouTube(url).streams
    result = ""
    resolution = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '144p']
    for i in resolution:
        try:
            k = yt.filter(res=i).desc().first().resolution[0:-1]
        except:
            k = None
        if k != None: 
            result += k + ' '
    return result + 'audio'


def choice_res(url: str):
    while True:
        match input(f'Enter resolution ({list_res(url)}): '):
            case '1080':
                return yt.filter(res='1080p', mime_type='video/mp4').desc().first()
            case '720':
                return yt.filter(type='video').get_by_resolution(resolution='720p')
            case '480':
                return yt.filter(res='480p').desc().first()
            case '360':
                return yt.filter(type='video').get_by_resolution(resolution='360p')
            case 'audio':
                return yt.filter(only_audio=True).desc().first()
            case 'exit':
                return


url = 'https://youtu.be/NsaouJxIbPA'
# url = user_input('url')
path = 'download'
# path = user_input('path to download catalog')

yt = YouTube(url, on_progress_callback=on_progress).streams
res = choice_res(url)
res.download(path)

exit()

# Download v.1.
# yt = pytube.YouTube(url)
# yt.streams.order_by('resolution').desc()
# yt = yt.streams[0].download()

# Download v.2.
# streams = pytube.YouTube(url).streams
# video_best = streams.order_by('resolution').desc().first()
# video = streams.order_by('resolution').desc()
# video_480 = streams.filter(res='480p').desc().first()
# audio_best = streams.filter(only_audio=True).desc().first()
# video_best.download()
# video.download()
# video_480.download()
# audio_best.download()

# Download v.3.
# streams = pytube.YouTube(url).streams
# stream = streams.get_by_itag(input('Number track: '))
# stream.download(path)

# Download v.4.
# yt = pytube.YouTube(url)
# yt.streams.order_by('resolution').desc()
# yt = yt.streams[0].download()

# Download the best video before 720p.
# video = streams.filter(progressive=True).desc().first()

# Print number of the resolution
# print(yt.filter(type='video').get_by_resolution(resolution='720p').resolution[0:-1]) # 720
# yt.streams.filter(type='video').get_highest_resolution().resolution[0:-1] # print high resolution

# Merge video and soundtrack for 1080 and high on Linux
# ffmpeg -i video.webm -i audio.webm -map 0:v -map 1:a -c copy out.webm
