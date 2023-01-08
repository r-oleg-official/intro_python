from pytube import YouTube
from pytube.cli import on_progress


def list_res(url: str) -> str:
    yt = YouTube(url).streams
    result = ""
    resolution = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '144p']
    for i in resolution:
        try:
            k = yt.filter(res=i).desc().first().resolution[0:-1]
        except:
            k = None
        if k is not None:
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


# url = 'https://youtu.be/NsaouJxIbPA'
url = input('Enter url: ')
# path = 'download'
path = input('Path to download catalog: ')
yt = YouTube(url, on_progress_callback=on_progress).streams
res = choice_res(url)
res.download(path)
video_best = yt.order_by('resolution').desc().first()
