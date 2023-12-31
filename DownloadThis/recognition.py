import pygame
import random


def assess(prediction, veritable_truth):
    exact = [False] * 5
    remains = []
    partial = []
    for q in range(5):
        if prediction[q] == veritable_truth[q]:
            exact[q] = True
    for t in range(5):
        if not exact[t]:
            remains.append(veritable_truth[t])
    for z in range(5):
        if prediction[z] in remains and not exact[z]:
            partial.append(True)
        else:
            partial.append(False)
        if partial[-1]:
            remains.remove(prediction[z])
    return exact, partial



def wordle(starting_words, num, key):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    user_text = ''
    font = pygame.font.Font(None, 110)
    clock = pygame.time.Clock()
    background = pygame.image.load('wordle.png')
    screen.blit(background, (0, 0))
    pygame.display.flip()
    word = num
    guesses = starting_words
    win_state = False
    games = 0
    correct = 0
    playing = True
    go_back = False
    while playing:
        start_time = pygame.time.get_ticks()
        with open('possible_answers') as possible_answers:
            content = possible_answers.readlines()
            randint = random.randint(0, 2309)
            answer = content[randint]
            parts = answer.split('\n')
            answer = parts[0]

        while not win_state:
            letter = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]

                    elif event.key == pygame.K_RETURN:
                        with open('possible_guesses') as possible_guesses:
                            if user_text.lower() in possible_guesses.read() and len(user_text) == 5:
                                guesses[word] = user_text

                                for character in user_text:
                                    x = 778 + letter * 70
                                    y = 225 + word * 95

                                    if character in answer:
                                        pygame.draw.rect(screen, (255, 196, 37), (x, y, 65, 90))

                                    for i in range(5):
                                        if user_text[i] == answer[i]:
                                            pygame.draw.rect(screen, (1, 154, 1), (x, y, 65, 90))

                                    letter += 1
                                word += 1
                            user_text = ''

                    elif len(user_text) < 5:
                        user_text += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 25 < x < 112 and 25 < y < 69:
                        go_back = True
                        win_state = True

            screen.blit(background, (0, 0))

            for character in user_text:
                x = 809 + letter * 70
                y = 270 + word * 95
                text_surface = font.render(character.lower(), True, (255, 255, 255))
                size = font.size(character)
                screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
                letter += 1

            for i in range(6):
                if guesses[i] != '':

                    letter = 0
                    green, yellow = assess(guesses[i], answer)

                    for k in range(5):

                        x = 809 + letter * 70
                        y = 270 + i * 95
                        color_x = x - 31
                        color_y = y - 45

                        if green[k]:
                            pygame.draw.rect(screen, (1, 154, 1), (color_x, color_y, 65, 90))

                        if yellow[k]:
                            pygame.draw.rect(screen, (255, 196, 37), (color_x, color_y, 65, 90))

                        text_surface = font.render(guesses[i][k].lower(), True, (255, 255, 255))
                        size = font.size(guesses[i][k])
                        screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
                        letter += 1

            if guesses[5] != '' and guesses[5] != answer:
                text = 'L + Bozo'
                text_surface = font.render(text, True, (150, 0, 0))
                width = text_surface.get_width()
                screen.blit(text_surface, (960 - width / 2, 850))
                text_surface = font.render(answer, True, (255, 255, 255))
                width, height = text_surface.get_width(), text_surface.get_height()
                screen.blit(text_surface, (960 - width / 2, 140 - height / 2))
                reset = pygame.image.load('reset.png')
                screen.blit(reset, (832, 925))
                games += 1
                win_state = True

            for guess in guesses:
                if guess == answer:
                    text = 'You Win!'
                    text_surface = font.render(text, True, (255, 255, 255))
                    screen.blit(text_surface, (790, 850))
                    win_state = True
                    games += 1
                    correct += 1
                    with open('recognition_top_times', 'r+') as top_times:
                        content = top_times.readlines()
                        for i in range(len(content)):
                            parts = content[i].split(' ')
                            try:
                                time = float(parts[1])
                            except IndexError:
                                time = 999999
                            except ValueError:
                                time = 999999
                            letters = parts[0]
                            real_word = letters.split('\n')
                            if answer == real_word[0] and round(counter, 2) < time:
                                content[i] = f'{answer}: {round(counter, 2)} \n'
                    open('recognition_top_times', 'w').close()
                    with open('recognition_top_times', 'w') as top_times:
                        top_times.writelines(content)

            end_time = pygame.time.get_ticks()
            counter = (end_time - start_time) / 1000
            timer_surface = font.render(str(round(counter, 2)), True, (255, 255, 255))
            width, height = timer_surface.get_width(), timer_surface.get_height()
            screen.blit(timer_surface, (430 - width / 2, 540 - height / 2))
            back_arrow = pygame.image.load('back_arrow.png')
            screen.blit(back_arrow, (25, 25))
            try:
                accuracy = correct / games
                accuracy_surface = font.render(str(round(accuracy, 2)), True, (255, 255, 255))
                width, height = accuracy_surface.get_width(), accuracy_surface.get_height()
                screen.blit(accuracy_surface, (1440 - width / 2, 540 - height / 2))
            except ZeroDivisionError:
                accuracy_surface = font.render('1', True, (255, 255, 255))
                width, height = accuracy_surface.get_width(), accuracy_surface.get_height()
                screen.blit(accuracy_surface, (1440 - width / 2, 540 - height / 2))
            label = font.render('Accuracy', True, (255, 255, 255))
            width, height = label.get_width(), label.get_height()
            screen.blit(label, (1440 - width / 2, 440 - height / 2))
            pygame.display.flip()
            clock.tick(60)

        while win_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if 805 < x < 1061 and 925 < y < 1053:
                        for i in range(6 - num):
                            starting_words.pop(num)
                        for k in range(6 - num):
                            starting_words.append('')
                        guesses = starting_words
                        screen.fill('BLACK')
                        screen.blit(background, (0, 0))
                        word = num
                        win_state = False

                    if 25 < x < 112 and 25 < y < 69:
                        playing = False
                        win_state = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.key.key_code(key):
                        for i in range(6 - num):
                            starting_words.pop(num)
                        for k in range(6 - num):
                            starting_words.append('')
                        guesses = starting_words
                        screen.fill('BLACK')
                        screen.blit(background, (0, 0))
                        word = num
                        win_state = False
            if go_back:
                playing = False
                win_state = False
            back_arrow = pygame.image.load('back_arrow.png')
            screen.blit(back_arrow, (25, 25))
            pygame.display.flip()
            clock.tick(60)
def startingWords(num):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    user_text = ''
    font = pygame.font.Font(None, 110)
    clock = pygame.time.Clock()
    pygame.display.flip()
    words = []
    error = ''
    while len(words) < num:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    with open('possible_guesses') as possible_guesses:
                        if user_text.lower() in possible_guesses.read() and len(user_text) == 5:
                            words.append(user_text)
                            error = 'Word Added!'
                        elif len(user_text) < 5:
                            error = 'Too Short!'
                        else:
                            error = 'Not a Word!'
                    user_text = ''
                elif len(user_text) < 5:
                    user_text += event.unicode
        pygame.draw.rect(screen, color, (0, 0, 1920, 1080))
        instruction_surface = font.render('Enter Starting Words', True, (255, 255, 255))
        width, height = instruction_surface.get_width(), instruction_surface.get_height()
        screen.blit(instruction_surface, (960 - width / 2, 340 - height / 2))
        error_surface = font.render(error, True, (255, 255, 255))
        width, height = error_surface.get_width(), error_surface.get_height()
        screen.blit(error_surface, (960 - width / 2, 440 - height / 2))
        user_surface = font.render(user_text, True, (255, 255, 255))
        width, height = user_surface.get_width(), user_surface.get_height()
        screen.blit(user_surface, (960 - width / 2, 540 - height / 2))
        pygame.display.flip()
        clock.tick(60)
    for i in range((6 - num)):
        words.append('')
    return words


def numStartingWords():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    user_text = ''
    font = pygame.font.Font(None, 110)
    clock = pygame.time.Clock()
    pygame.display.flip()
    num = 0
    error = ''
    while num == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        if 0 < int(user_text) < 6:
                            num = int(user_text)
                        else:
                            error = 'Too Big!'
                            user_text = ''
                    except ValueError:
                        error = 'Not a Number!'
                        user_text = ''
                else:
                    user_text += event.unicode
        pygame.draw.rect(screen, color, (0, 0, 1920, 1080))
        instruction_surface = font.render('Enter Number of Starting Words', True, (255, 255, 255))
        width, height = instruction_surface.get_width(), instruction_surface.get_height()
        screen.blit(instruction_surface, (960 - width / 2, 340 - height / 2))
        user_surface = font.render(user_text, True, (255, 255, 255))
        width, height = user_surface.get_width(), user_surface.get_height()
        screen.blit(user_surface, (960 - width / 2, 540 - height / 2))
        error_surface = font.render(error, True, (255, 255, 255))
        width, height = error_surface.get_width(), error_surface.get_height()
        screen.blit(error_surface, (960 - width / 2, 440 - height / 2))
        pygame.display.flip()
        clock.tick(60)
    return num

