import audio_analysis as an
import openai_connection as opc
import leonardo_connection as lc
from downloads import download_image
from credentials import Credentials


def test_openai():
    my_credentials = Credentials()
    openai_key = my_credentials.openai_key
    openai_client = opc.My_OpenAI(openai_key)
    name = an.record_audio()
    prompt = an.speech_to_text(name, openai_key)
    print(prompt)
    # an.delete_audio(nombre)
    img_url = openai_client.generate_image(prompt)
    image_name = download_image(img_url, "OpenAI")
    response = input("Do you want to generate a variation of the last photo?")
    if response == "yes" or response == "Yes":
        openai_client.generate_variation(image_name)
    else:
        exit()


def test_leonardo():
    my_credentials = Credentials()
    my_leonardo = lc.My_Leonardo(my_credentials.leonardo_key)
    user_info = my_leonardo.get_user_info()
    user_id = user_info["user_details"][0]["user"]["id"]

    image_url = my_leonardo.image_generation(
        prompt="A blonde girl with brilliant long hair, blue eyes. The face must be the more beautiful that have "
               "never existed." +
               "She is wearing a top with jeans. Her body estructure is like a top model.")

    return image_url


def full_test():
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
