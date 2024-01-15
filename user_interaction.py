import audio_analysis as an
import credentials as cs
import openai_connection as opc
import leonardo_connection as lc


def test_openai():
    openai_key = cs.Credentials.OPENAI
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

def test_leonardo():
    my_leonardo = lc.My_Leonardo(cs.Credentials.LEONARDO)
    user_info = my_leonardo.get_user_info()
    user_id = user_info["user_details"][0]["user"]["id"]

    image_url = my_leonardo.image_generation(prompt="A blonde girl with brilliant long hair, blue eyes. The face must be the more beautiful that have never existed."+
                    "She is wearing a top with jeans. Her body estructure is like a top model.")

    return image_url