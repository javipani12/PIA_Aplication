import audio_analysis as an

nombre = an.record_audio()
print(an.speech_to_text(nombre))
an.delete_audio(nombre)
