import os
import pyaudio
import wave
from datetime import datetime


def record_audio():
    """
    This function is used to record an audio_and_text in .wav format

    :return: (String) File name of the created audio_and_text
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


def speech_to_text(audio_name, openai_client, language):
    """
    Method to transform an audio_and_text to text

    :param audio_name: (String) File name of the audio_and_text to transcript
    :param openai_client: (String) The OpenAI client
    :param language: (String) The language to transcript the audio_and_text
    :return: (String) The generated transcription
    """
    audio_file = open(audio_name, "rb")
    print("Generating the transcription...")
    transcript = openai_client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text",
        language=language
    )
    print("Transcription generated successfully...")

    return transcript


def delete_audio(audio_name):
    """
    Method to delete an audio_and_text

    :param audio_name: (String) File name of the audio_and_text to delete
    """
    os.remove(audio_name)
