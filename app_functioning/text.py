import translators as ts
import json
import os

def improve_prompt(prompt, language):
    """
    This function is used to improve the prompt for the image generation

    :param prompt: (String) Text generated from audio_and_text
    :param language: (String) The language to translate the improved prompt
    :return: (String) Improved text for prompt
    """

    if language == 'es':
        if "niños" in prompt:
            return create_improved_prompt(prompt, "niños")
        elif "" in prompt:
            return create_improved_prompt(prompt, "")
    else:
        if translate_key_word("niños", language) in prompt:
            return create_improved_prompt(prompt, "niños", False, language)
        elif translate_key_word("", language) in prompt:
            return create_improved_prompt(prompt, "", False, language)


def create_improved_prompt(prompt, key_word, original_lan=True, language='es'):
    """
    Function to create an improved prompt for the image generation, giving more details
    about the photo to help AIs to generate a better pic.

    :param prompt: (String) The text that will be improved
    :param key_word: (String) It depends on this word what type will be the improved prompt
    :param original_lan: (Boolean) It determines if the language is spanish or other one
    :param language: (String) Language to translate the content of the improved prompt
    :return: (String) The generated improved prompt
    """
    content = ""
    dictionary = {}
    if not os.path.exists("media/json/prompt.json"):
        if key_word == "niños":
            content = "Estilo infantil, detallado, con colores vivos y buena resolución"
        elif key_word == "":
            content = ""
    else:
        with open("media/json/prompt.json") as file:
            dictionary = json.load(file)

        if key_word in dictionary.keys():
            content = dictionary[key_word]

    if original_lan:
        improved_prompt = prompt + content
    else:
        content_translated = ts.translate_text(query_text=content, from_language='es', to_language=language)
        improved_prompt = prompt + content_translated

    return improved_prompt


def translate_key_word(key_word, language):
    """
    Function to translate the word that will be searched on prompt

    :param key_word: (String) The word that will be searched
    :param language: (String) Language to translate the word
    :return: (String) Returns the translated word
    """
    return ts.translate_text(query_text=key_word, from_language='es', to_language=language)
