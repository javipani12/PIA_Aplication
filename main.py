from user_interaction import html_generation as html
from audio import audio_analysis as an
from connections import leonardo_connection as lc, openai_connection as opc
from download.downloads import download_image
from credentials.credentials import Credentials

my_credentials = Credentials()
openai_client = opc.My_OpenAI(my_credentials.openai_key)
leonardo_client = lc.My_Leonardo(my_credentials.leonardo_key)

audio_name = an.record_audio()
prompt = an.speech_to_text(audio_name, openai_client.openai_key)

img_url_openai = openai_client.generate_image(prompt)
img_url_leonardo = leonardo_client.image_generation(prompt)

img_openai = download_image(img_url_openai, "OpenAI")
img_leonardo = download_image(img_url_leonardo, "Leonardo")

an.delete_audio(audio_name)
