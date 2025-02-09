with open('change.txt', 'r') as f:
    content = f.readlines()
    with open('possible_guesses.txt', 'w') as f2:
        for line in content:
            try:
                f2.write(line.split('"')[1].lower())
                f2.write('\n')
            except IndexError:
                print(line)
