from user_interaction import html_generation as html
from audio_and_text import audio_analysis as an, text_analysis as tx
from connections import leonardo_connection as lc, openai_connection as opc
from download.downloads import download_image
from credentials.credentials import Credentials

my_credentials = Credentials()
openai_client = opc.My_OpenAI(my_credentials.openai_key)
leonardo_client = lc.My_Leonardo(my_credentials.leonardo_key)

audio_name = an.record_audio()
prompt = an.speech_to_text(audio_name, openai_client.openai_client, my_credentials.language)
improved_prompt = tx.improve_prompt(prompt, my_credentials.language)
print(improved_prompt)

img_url_openai = openai_client.generate_image(improved_prompt)
img_url_leonardo = leonardo_client.image_generation(improved_prompt)

img_openai = download_image(img_url_openai, "OpenAI")
img_leonardo = download_image(img_url_leonardo, "Leonardo")

an.delete_audio(audio_name)
