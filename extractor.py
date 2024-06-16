from pytube import YouTube
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

from transcript import transcribe
from claude import translateText

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=False).first()
    video.download(output_path=output_path)
    return video.default_filename


def extract_audio(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    video_clip.audio.write_audiofile(audio_path)


def extract(video_url):
    # video_url = "https://www.youtube.com/watch?v=_N6j8HXPt2U" #payload
    output_path = "./"
    video_filename = download_youtube_video(video_url, output_path)
    extract_audio(output_path + video_filename, output_path + "audio.wav")
    convertChannel()
    transcribe_text = transcribe(file_name='audio_1m.wav')
    translated_text = translateText(transcribe_text)
    resultObj = {"transcribed":transcribe_text,"translated":translated_text}
    return resultObj


def convertChannel():
    sound = AudioSegment.from_wav("audio.wav")
    sound = sound.set_channels(1)
    sound.export("audio_1m.wav", format="wav")
