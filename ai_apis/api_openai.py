from openai import OpenAI, BadRequestError
from app_functioning.downloads import download_image


class My_OpenAI:
    def __init__(self, openai_key):
        self.openai_key = openai_key
        self.openai_client = OpenAI(api_key=self.openai_key)

    def generate_image(self, prompt):
        """
        This function is used to generate an image on Leonardo based on a prompt

        :param prompt: (String) The generation of the image is based on this text
        :return: (String) URL of the generated image
        """
        print("Generating the image with OpenAI...")
        try:
            response = self.openai_client.images.generate(
                model="dall-e-2",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            print("Image generated successfully...")
        except Exception as ex:
            print("An exception occurred", ex)
            exit()
        return response.data[0].url

    def generate_variation(self, file_name):
        """
        Function to generate a variation of an image
        :param file_name: (String) File name of the image to generate the variation
        """
        print("Generating a variation of the original image of OpenAI...")
        response = self.openai_client.images.create_variation(
            image=open(file_name, "rb"),
            n=2,
            size="1024x1024"
        )
        image_url = response.data[0].url
        print("Variation image generated successfully...")
        download_image(image_url, "OpenAI", True, file_name)

    def speech_to_text(self, audio_name, language):
        """
        Method to transform an audio_and_text to text

        :param audio_name: (String) File name of the audio_and_text to transcript
        :param language: (String) The language to transcript the audio_and_text
        :return: (String) The generated transcription
        """
        audio_file = open(audio_name, "rb")
        try:
            transcript = self.openai_client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text",
                language=language
            )
            print("Generating the transcription...")
        except Exception as ex:
            print("An error occurred", ex)
            exit()
        print("Transcription generated successfully...")

        return transcript
