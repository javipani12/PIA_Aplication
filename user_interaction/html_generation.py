# This is used to get the image's absolute path
import os
# This is used to set the html name.
from datetime import datetime
# Library that is used to open a html file.
import webbrowser


def generate_html(openai_image, leonardo_image):
    """
    Function to generate an HTML page with the generated photos

    :param openai_image: (String) It contains the name of the OpenAi generated image
    :param leonardo_image: (String) It contains the name of the Leonardo generated image

    :return: (String) Returns the file path of the HTML generated file
    """

    now = datetime.now()
    # Create the full path of the images
    full_path_openai = os.path.abspath(openai_image)
    full_path_leonardo = os.path.abspath(leonardo_image)

    html_page = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Tabla con Imágenes</title>
                <style>
                    body {{
                        background-color: #f5f5f5;
                    }}
                    table {{
                        width: 100%; 
                        border-collapse: collapse;
                        background-color: #e0e0e0;
                    }}
                    th, td {{
                        border: 2px solid #777;
                        padding: 8px;
                        text-align: center;
                    }}
                    th {{
                        background-color: #333;
                        color: #fff;
                    }}
                    th span {{
                        color: #ffcc00;
                    }}
                    td {{
                        background-color: #f2f2f2;
                    }}
                </style>
            </head>
            <body>

            <table>
                <tr>
                    <th><span>OpenAI</span></th>
                    <th><span>Leonardo</span></th>
                </tr>
                <tr>
                    <td><img src="{full_path_openai}" alt="OpenAI" style="width: 100%; height: auto;"></td>
                    <td><img src="{full_path_leonardo}" alt="Leonardo" style="width: 100%; height: auto;"></td>
                </tr>
            </table>

            </body>
            </html>
        """

    file_name = "media/html/" + now.strftime("%d%m%y_%H%M%S") + ".html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_page)

    return file_name


def open_html_file(file_name):
    """
    Function to open an HTML page on the browser

    :param file_name: (String) Name of the file to be opened
    """
    full_path = os.path.abspath(file_name)
    file_url = f'file://{full_path}'
    webbrowser.open(file_url, new=2)
