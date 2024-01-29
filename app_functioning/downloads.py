from datetime import datetime
import requests
from PIL import Image


def download_image(url, ai, variation=False, name=""):
    """
    This method is used to download an image using its URL

    :param url: (String) URL of the image to download
    :param ai: (String) This param indicates which AI has generated the photo
    :param variation: (Boolean) It's used to determinate if the photo of the URL
    is a new one or a variation of other one
    :param name: (String) If variation is True, then this variable will be used to create
    the name of the image based on name of the original photo
    :return:
    """
    now = datetime.now()
    data = requests.get(url).content

    if variation:
        # If it's a variation image from the original, we get the name of it
        file_name = name.split(".")[0] + "_variation." + name.split(".")[1]
    else:
        # If it's a new image, we create a name for it
        file_name = f"media/images/{ai}_" + now.strftime("%d%m%y_%H%M%S") + ".png"

    file = open(file_name, "wb")
    file.write(data)

    return file_name
