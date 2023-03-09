import moviepy.editor as mp
import speech_recognition as sr


# clipにvideo()を代入
clip = mp.VideoFileClip('video_recording.mov') 
# clipからaudioを抜き出し、converted_audio.wavとして保存する
clip.audio.write_audiofile('converted_audio.wav')  