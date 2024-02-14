# This is used to set a name to the image.
from datetime import datetime
# This library is used to download the image.
import requests


def download_image(url, ai):
    """
    This method is used to download an image using its URL

    :param url: (String) URL of the image to download
    :param ai: (String) This param indicates which AI has generated the photo
    :return: (String) The file name of the downloaded image
    """
    now = datetime.now()
    data = requests.get(url).content

    file_name = f"media/images/{ai}_" + now.strftime("%d%m%y_%H%M%S") + ".png"

    file = open(file_name, "wb")
    file.write(data)

    return file_name
