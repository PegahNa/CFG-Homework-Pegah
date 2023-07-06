# Move the first letter of each word to the end of it, then add "ay" to the end of the
# word. Leave punctuation marks untouched.

def pig_it(text):
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word.isalpha():
            pig_latin_word = word[1:] + word[0] + 'ay'
        else:
            pig_latin_word = word

        pig_latin_words.append(pig_latin_word)

    return ' '.join(pig_latin_words)
