from datetime import datetime


def generate_html(openai_image, leonardo_image):
    """
    Function to generate an HTML page with the generated photos

    :return:
    """
    now = datetime.now()
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
                <td style="border: 1px solid #ddd; padding: 8px;"><img src"{openai_image}" alt="OpenAI" style="width: 100%; height: auto;"></td>
                <td style="border: 1px solid #ddd; padding: 8px;"><img src="{leonardo_image}" alt="Leonardo" style="width: 100%; height: auto;"></td>
            </tr>
        </table>
        
        </body>
        </html>
    """

    file_name = now.strftime("%d%m%y_%H%M%S") + ".html"
    file = open(file_name, "w")
    file.write(html_page)




