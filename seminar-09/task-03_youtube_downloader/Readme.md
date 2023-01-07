## Install.
Need install Pythonlib - `pytube`:

    pip3 install pytube

## Use.
Run this script. For downloading:
1. Enter url video, example, `https://youtu.be/NsaouJxIbPA`;
2. Enter path to catalog for save video;
3. Choice video quality.

## Download in FullHD quality.

1. Choice video quality `1080`;
2. Choice `audio` for downloading a audio track in `*.webm`;
3. Merge video and soundtrack for 1080 and high on Linux, 

Example, `ffmpeg` into terminal:<br>

    ffmpeg -i video.mp4 -i audio.webm -map 0:v -map 1:a -c copy out.mkv 
	ffmpeg -i video.mp4 -i audio.webm -sctrict -2 -map 0:v -map 1:a -c copy out.mp4
