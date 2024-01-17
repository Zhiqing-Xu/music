import os
from pydub import AudioSegment

def convert_wav_to_mp3(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a WAV file
        if filename.endswith(".wav"):
            wav_path = os.path.join(directory, filename)
            
            # Load the WAV file
            wav_audio = AudioSegment.from_file(wav_path, format="wav")

            # Define the MP3 file path
            mp3_path = os.path.join(directory, os.path.splitext(filename)[0] + ".mp3")
            
            # Convert and save as MP3
            wav_audio.export(mp3_path, format="mp3")
            print(f"Converted '{wav_path}' to '{mp3_path}'")

# Provide your directory path here
            
directory_path = ["./Other/FuBao/assets_music/music" ,
                  "./WenDu/assets_music/music"       ,
                  "./BiXin/assets_music/music"       ,
                  "./FanTing/assets_music/music"     ,
                  ""                                 ,
                  ][1]




convert_wav_to_mp3(directory_path)
