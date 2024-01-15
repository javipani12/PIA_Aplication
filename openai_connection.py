from openai import OpenAI

class My_OpenAI:

    def __init__(self, openai_key):
        self.openai_key = openai_key
        self.openai_client = OpenAI(api_key=self.openai_key)

    def generate_image(self, prompt):
        response = self.openai_client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        return response.data[0].url

    

    def generate_variation(self, file_name):
        response = self.openai_client.images.create_variation(
            image=open(file_name, "rb"),
            n=2,
            size="1024x1024"
        )
        image_url = response.data[0].url

        My_OpenAI.download_image(image_url, True, file_name)
