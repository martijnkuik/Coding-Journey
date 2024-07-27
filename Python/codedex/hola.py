def translator(language):
    # Create a dictionary for different languages
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'},
        'dutch': {'hello': 'hallo', 'goodbye': 'tot ziens', 'thank you': 'dank je'},
        'german': {'hello': 'hallo', 'goodbye': 'auf wiedersehen', 'thank you': 'danke'},
        'greek': {'hello': 'γειά σου', 'goodbye': 'αντίο', 'thank you': 'ευχαριστώ'},
        'polish': {'hello': 'cześć', 'goodbye': 'do widzenia', 'thank you': 'dziękuję'}
    }

    def translate_word(word):
        word_lower = word.lower()
        if language in translations:
            if word_lower in translations[language]:
                return translations[language][word_lower]
            else:
                return 'Translation not available'
        else:
            return 'Language not supported'

    return translate_word

# Example usage:
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))  # Output: hola

translate_to_french = translator('french')
print(translate_to_french('hello'))  # Output: bonjour

translate_to_italian = translator('italian')
print(translate_to_italian('hello'))  # Output: ciao

translate_to_dutch = translator('dutch')
print(translate_to_dutch('hello'))  # Output: hallo

translate_to_german = translator('german')
print(translate_to_german('hello'))  # Output: hallo

translate_to_greek = translator('greek')
print(translate_to_greek('hello'))  # Output: γειά σου

translate_to_polish = translator('polish')
print(translate_to_polish('hello'))  # Output: cześć


# Comment on how to input Greek and Polish characters:
# Greek Characters: You can input Greek characters using a Greek keyboard layout or by using Unicode character codes.
# For example, 'γειά σου' (hello) can be typed as 'γειά σου' on a Greek keyboard.
# Alternatively, you can use Unicode escape sequences, e.g., '\u03b3\u03b5\u03b9\u03ac \u03c3\u03bf\u03c5'.

# Polish Characters: You can input Polish characters using a Polish keyboard layout or by using Unicode character codes.
# For example, 'cześć' (hello) can be typed as 'cześć' on a Polish keyboard.
# Alternatively, you can use Unicode escape sequences, e.g., 'cze\u015b\u0107'.
