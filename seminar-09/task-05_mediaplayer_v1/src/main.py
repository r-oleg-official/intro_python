import vlc
import time


def main():
    # Create the vlc media player object
    media_player = vlc.MediaPlayer()
    media = vlc.Media("example.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(0.1)
    dur = (media_player.get_length()) / 1000
    media_player.play()
    time.sleep(dur)


if __name__ == "__main__":
    main()
