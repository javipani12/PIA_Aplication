from datetime import datetime
import requests
from PIL import Image


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