import requests
from PIL import Image
from openai import OpenAI
from datetime import datetime


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

    @staticmethod
    def download_image(url, edit=False, name=""):
        now = datetime.now()
        data = requests.get(url).content

        if edit:
            # If it's an edited image, we get the name of it
            file_name = name.split(".")[0] + "_edit." + name.split(".")[1]
        else:
            # If it's a new image, we create a name for it
            file_name = "images/" + now.strftime("%d%m%y_%H%M%S") + ".png"

        file = open(file_name, "wb")
        file.write(data)

        img = Image.open(file_name)
        img.show()

        return file_name

    def generate_variation(self, file_name):
        response = self.openai_client.images.create_variation(
            image=open(file_name, "rb"),
            n=2,
            size="1024x1024"
        )
        image_url = response.data[0].url

        My_OpenAI.download_image(image_url, True, file_name)
