
from moviepy.editor import *

def create_video(audio):
    clips = [
        VideoFileClip("stock.mp4").subclip(0,10),
        VideoFileClip("stock.mp4").subclip(10,20)
    ]
    final = concatenate_videoclips(clips)

    audio_clip = AudioFileClip(audio)
    final = final.set_audio(audio_clip).subclip(0, audio_clip.duration)

    final.write_videofile("final_video.mp4", fps=24)
    return "final_video.mp4"
