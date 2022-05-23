import deepl


def translate(key: str, target_lang: str, text: str, source_lang=None or str):
    translator = deepl.Translator(key)
    result = translator.translate_text(text,
                                       source_lang=source_lang,
                                       target_lang=target_lang,
                                       formality="default")
    return result.text
