import json


with open('wordlist.json', 'r') as f:
    data = json.load(f)

    with open('possible_answers.txt', 'w') as f2:
        for word in data['default']:
            f2.write(word.lower() + '\n')

    with open('possible_guesses.txt', 'w') as f2:
        for word in data['valid']:
            f2.write(word.lower() + '\n')
