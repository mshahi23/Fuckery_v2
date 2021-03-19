from pytube import Playlist
from moviepy.editor import *
import os
import ffmpeg


bad_chars = ['/', "\\", ':', '*', '?', '"', '<', '>', '|', "'", "."]
# Output type
download_status = True
gif_status = False
mp3_status = False
delete_original = False
insane_quality = False


def intro(url, filetype, quality):
    global link
    global delete_original
    global download_status
    global gif_status
    global mp3_status
    global insane_quality

    if not url == "":
        link = url
    if filetype == "" or filetype == "mp4":
        delete_original = False
    if filetype == "mp3":
        mp3_status = True
    if filetype == "gif":
        gif_status = True
    if quality == "yes" or quality == "y":
        insane_quality = True

    p = Playlist(link)

    for video in p.videos:
        print(f'Downloading: {video.title}')
        # print(video.streams.all())
        trackName = video.title
        if download_status:
            print("Sucking data from youtube, please be patient")
            path_raw_video = './raw-video'
            path_raw_audio = './raw-audio'
            path_mp4 = './mp4'
            missing_dir(path_mp4)

            for i in bad_chars:
                trackName = trackName.replace(i, '')
            mp4_file = './mp4/%s.mp4' % trackName
            if insane_quality:
                missing_dir(path_raw_video)
                missing_dir(path_raw_audio)
                video.streams.filter(res="1080p").first().download(path_raw_video)
                video.streams.filter(abr="160kbps").first().download(path_raw_audio)
                input_video = ffmpeg.input('./raw-video/%s.mp4' % trackName)
                input_audio = ffmpeg.input('./raw-audio/%s.webm' % trackName)
                ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./mp4/%s.mp4' % trackName).run()
            else:
                video.streams.filter().first().download(path_mp4)
            our_video = VideoFileClip(mp4_file)
            our_audio = our_video.audio
            if mp3_status:
                path_mp3 = './mp3'
                missing_dir(path_mp3)
                mp3_file = './mp3/%s.mp3' % trackName
                our_audio.write_audiofile(mp3_file)
            if gif_status:
                path_gif = './gif'
                missing_dir(path_gif)
                gif_file = './gif/%s.gif' % trackName
                our_video.write_gif(gif_file)
            try:
                our_audio.close()
                our_video.close()
            except:
                print("Closed files")
            else:
                print("Closed files")
        if delete_original:
            os.remove('./mp4/%s.mp4' % trackName)


def missing_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        message = "You are missing a directory so we made it for you"
        return message
