text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words = text.split()

new_words = []

for word in words:
    if word.endswith(','):
        new_word = word[:-1] + 'ing' + ','
    elif word.endswith('.'):
        new_word = word[:-1] + 'ing' + '.'
    else:
        new_word = word + 'ing'

    new_words.append(new_word)

new_text = ' '.join(new_words)

print(new_text)
