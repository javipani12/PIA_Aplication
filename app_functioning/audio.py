# Library is used to remove files.
import os
# These libraries are used to record and save the audio.
import pyaudio
import wave
from datetime import datetime


def record_audio():
    """
    This function is used to record an audio in .wav format
    It was developed in class.

    :return: (String) File name of the created audio
    """
    chunk = 1024  # Record in samples of 1024 fragments
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2  # Use 2 channels to record
    fs = 44100  # Record 44100 samples per second
    p = pyaudio.PyAudio()  # Create an instance of PyAudio

    try:
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)
        print('Recording...')
    except Exception as ex:
        print("An error occurred", ex)
        exit()
    frames = []  # Initialize the array which would contains the frames

    # Keep the data on the chunks for the indicated time (in seconds)
    for i in range(0, int(fs / chunk * 7)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream and teminate the instances of PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('Record has been finished')

    # Store the record as a WAV archive whose name use the current datetime.
    now = datetime.now()
    audio_name = "media/audios/" + now.strftime("%d%m%y_%H%M%S") + ".wav"
    wf = wave.open(audio_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    return audio_name


def delete_audio(audio_name):
    """
    Method to delete an audio

    :param audio_name: (String) File name of the audio to delete
    """
    os.remove(audio_name)
