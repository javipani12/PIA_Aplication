import audio_analysis as an
import credentials as cr
import openai_connection as opc


def test():
    openai_key = cr.Credentials.OPENAI
    openai_client = opc.My_OpenAI(openai_key)
    name = an.record_audio()
    prompt = an.speech_to_text(name, openai_key)
    print(prompt)
    # an.delete_audio(nombre)
    img_url = openai_client.generate_image(prompt)
    image_name = openai_client.download_image(img_url)
    response = input("Do you want to generate a variation of the last photo?")
    if response == "yes" or response == "Yes":
        openai_client.generate_variation(image_name)
    else:
        exit()
