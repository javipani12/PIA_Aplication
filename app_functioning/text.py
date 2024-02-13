# Library that is used to translate text.
import translators as ts
# This is used to load the different stored keywords
# in json file.
import json


def improve_prompt(prompt, language):
    """
    This function is used to improve the prompt for the image generation

    :param prompt: (String) Text generated from the transcription
    :param language: (String) The language to translate the prompt
    :return: (String) Returns the generated improved prompt
    """
    counter = 0

    with open("media/json/prompt.json", encoding="utf-8") as file:
        dictionary = json.load(file)

    for word in dictionary.keys():
        if language == 'es':
            if word in prompt:
                counter += 1
                return create_improved_prompt(prompt, dictionary, word)
        else:
            if translate(word, language) in prompt:
                counter += 1
                return create_improved_prompt(prompt, dictionary, word, False, language)

    if counter == 0:
        return prompt


def create_improved_prompt(prompt, prompt_dictionary, key_word, original_lan=True, language='es'):
    """
    This function selects the details for the improved prompt based on the key word

    :param prompt: (String) The text that will be improved
    :param prompt_dictionary: (Dict) Dictionary that contains the details related to the keywords
    :param key_word: (String) It depends on this word which details will be selected on prompt_dictionary
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
