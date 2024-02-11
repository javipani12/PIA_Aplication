from openai import OpenAI


class My_OpenAI:
    def __init__(self, openai_key):
        self.openai_key = openai_key
        self.openai_client = OpenAI(api_key=self.openai_key)

    def generate_image(self, prompt):
        """
        This function is used to generate an image on OpenAI based on a prompt

        :param prompt: (String) The text to generate the image
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

    def speech_to_text(self, audio_name, language):
        """
        Method to transform an audio to text

        :param audio_name: (String) File name of the audio to transcript
        :param language: (String) The language to transcript the audio
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
