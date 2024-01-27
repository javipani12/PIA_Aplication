import translators as ts
import json


def improve_prompt(prompt, language):
    """
    This function is used to improve the prompt for the image generation

    :param prompt: (String) Text generated from audio_and_text
    :param language: (String) The language to translate the improved prompt
    :return: (String) Improved text for prompt
    """

    with open("media/json/prompt.json") as file:
        dictionary = json.load(file)

    for word in dictionary.keys():
        if language == 'es':
            if word in prompt:
                return create_improved_prompt(prompt, dictionary, word)
        else:
            if translate(word, language) in prompt:
                return create_improved_prompt(prompt, dictionary, word, False, language)


def create_improved_prompt(prompt, prompt_dictionary, key_word, original_lan=True, language='es'):
    """
    Function to create an improved prompt for the image generation, giving more details
    about the photo to help AIs to generate a better pic.

    :param prompt_dictionary: (Dict) Dictionary that contains the improved prompt related to the keywords
    :param prompt: (String) The text that will be improved
    :param key_word: (String) It depends on this word what type will be the improved prompt
    :param original_lan: (Boolean) It determines if the language is spanish or other one
    :param language: (String) Language to translate the content of the improved prompt
    :return: (String) The generated improved prompt
    """

    if original_lan:
        improved_prompt = prompt + prompt_dictionary[key_word]
    else:
        content_translated = translate(prompt_dictionary[key_word], language)
        improved_prompt = prompt + content_translated

    return improved_prompt


def translate(text, language):
    """
    Function to translate a text

    :param text: (String) Text that will be translated
    :param language: (String) Language to translate the text
    :return: (String) Returns the translated text
    """
    return ts.translate_text(query_text=text, from_language='es', to_language=language)
