from googletrans import Translator

# Create an instance of the Translator
translator = Translator()

# Define a function to translate text
def translate_text(text, src_lang='auto', dest_lang='en'):
    """
    Translate text from one language to another.

    :param text: str, the text to translate
    :param src_lang: str, source language (default is 'auto' for automatic detection)
    :param dest_lang: str, destination language (default is 'en' for English)
    :return: str, translated text
    """
    try:
        # Perform the translation
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Sample text to translate
    text = "Bonjour tout le monde"
    translated_text = translate_text(text, dest_lang='en')
    print(f"Translated text: {translated_text}")