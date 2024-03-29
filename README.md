# PIA_Aplication

# Description
This application allows you to generate some images with OpenAI and Leonardo with your voice.

# Installation and usage
> [!WARNING]
> It is necessary to have a valid account of OpenAI and Leonardo to use this application

To install the project you have to download the ZIP file, unzip it and open it on your favourite environment that allows Python.
Then on the path of the project, you have to create a new file called ".env" that will contain these lines:

    LANGUAGE = "<your_language>"
    OPENAI = "<your_openai_api_key>"
    LEONARDO = "<your_leonardo_api_key>"

To know the available languages check the next [link](https://github.com/openai/whisper#available-models-and-languages)

> [!CAUTION]
> Probably you will have to install some packages that the project will mark as warnings.

Then connect your microphone to your computer. Now you are prepared to use the application by running the file "main.py".

# Libraries documentation
Here we leave the links with official documentation of apis we have used in the project:
    
`Text to speech`: [Documentation](https://platform.openai.com/docs/guides/text-to-speech)

`DALL-E 2`: [Documentation](https://platform.openai.com/docs/guides/images/image-generation?context=node)

`Leonardo AI`: [Documentation](https://pypi.org/project/leonardo-api/)
    
# Authors :technologist:
| [<img src="https://avatars.githubusercontent.com/u/117437024?v=4" width=115><br><sub>Diego Castilla Saez</sub>](https://github.com/DiegoCS77) | [<img src="https://avatars.githubusercontent.com/u/117436698?v=4" width=115><br><sub>Javier Fernández Paniagua</sub>](https://github.com/javipani12) |
|:--------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
