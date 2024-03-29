# Importing the different files we have created.
from user_interaction import html_generation as html
from ai_apis import api_openai as aop, api_leonardo as al
from app_functioning import text as tx, audio as au
from app_functioning.downloads import download_image
from app_functioning.credentials import Credentials

# Setting connection with credentials to the different apis.
my_credentials = Credentials()
openai_client = aop.My_OpenAI(my_credentials.openai_key)
leonardo_client = al.My_Leonardo(my_credentials.leonardo_key)
language = my_credentials.language

# Audio saved and prompt generation.
audio_name = au.record_audio()
prompt = openai_client.speech_to_text(audio_name, language)
improved_prompt = tx.improve_prompt(prompt, language)

# Image generation based on the prompt.
img_url_openai = openai_client.generate_image(improved_prompt)
img_url_leonardo = leonardo_client.image_generation(improved_prompt)

# Images downloaded.
img_openai = download_image(img_url_openai, "OpenAI")
img_leonardo = download_image(img_url_leonardo, "Leonardo")

# html file generated and opened.
html_name = html.generate_html(img_openai, img_leonardo)
html.open_html_file(html_name)

# Audio file is deleted.
au.delete_audio(audio_name)
