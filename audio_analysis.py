import os
from openai import OpenAI
import pyaudio
import wave
from datetime import datetime


# This method is used to record an audio in .wav format
def record_audio():
    chunk = 1024                        # Record in samples of 1024 fragments
    sample_format = pyaudio.paInt16     # 16 bits per sample
    channels = 2                        # Use 2 channels to record
    fs = 44100                          # Record 44100 samples per second
    p = pyaudio.PyAudio()               # Create an instance of PyAudio

    print('Recording...')
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []     # Initialize the array which would contains the frames

    # Keep the data on the chunks for the indicated time (in seconds)
    for i in range(0, int(fs / chunk * 7)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream and teminate the instances of PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('Record has been finished')

    # Store the record as a WAV archive
    now = datetime.now()
    audio_name = "audios/" + now.strftime("%d%m%y_%H%M%S") + ".wav"
    wf = wave.open(audio_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    return audio_name


# Method to transform an audio to text
def speech_to_text(audio_name, openai_key):
    client = OpenAI(api_key=openai_key)
    audio_file = open(audio_name, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text",
        language="es"
    )

    return transcript

# Method to delete an audio
def delete_audio(audio_name):
    os.remove(audio_name)
