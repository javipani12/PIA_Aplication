import os
from datetime import datetime
import webbrowser


def generate_html(openai_image, leonardo_image):
    """
    Function to generate an HTML page with the generated photos

    :return:
    """

    now = datetime.now()
    full_path_openai = os.path.abspath(openai_image)
    full_path_leonardo = os.path.abspath(leonardo_image)

    html_page = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tabla con Imágenes</title>
        </head>
        <body>
        
        <table style="width:100%; border-collapse: collapse;">
            <tr>
                <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">OpenAI</th>
                <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Leonardo</th>
            </tr>
            <tr>
                <td style="border: 1px solid #ddd; padding: 8px;"><img src="{full_path_openai}" alt="OpenAI" style="width: 100%; height: auto;"></td>
                <td style="border: 1px solid #ddd; padding: 8px;"><img src="{full_path_leonardo}" alt="Leonardo" style="width: 100%; height: auto;"></td>
            </tr>
        </table>
        
        </body>
        </html>
    """

    file_name = "media/html/" + now.strftime("%d%m%y_%H%M%S") + ".html"
    file = open(file_name, "w")
    file.write(html_page)

    return file_name


def open_html_file(file_name):
    """
    Function to open an HTML page on browser

    :param file_name: (String) Name of the file to be opened
    """
    full_path = os.path.abspath(file_name)
    file_url = f'file://{full_path}'
    webbrowser.open(file_url, new=2)
