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


def lateGame(starting_words, num, key):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    user_text = ''
    font = pygame.font.Font(None, 80)
    clock = pygame.time.Clock()
    background = pygame.image.load('late_game.png')
    back_arrow = pygame.image.load('back_arrow.png')
    screen.blit(background, (0, 0))
    pygame.display.flip()
    word = 12
    guesses = starting_words
    for i in range(6 - num):
        guesses.pop(num)
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
            for i in range(11 - num):
                randint = random.randint(0, 2309)
                yaya = content[randint]
                parts = yaya.split('\n')
                guesses.append(parts[0])
            guesses.append('')

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
                                guesses[11] = user_text
                        user_text = ''
                    elif len(user_text) < 5:
                        user_text += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 25 < x < 112 and 25 < y < 69:
                        go_back = True
                        win_state = True

            screen.fill(color)
            screen.blit(background, (0, 0))

            for character in user_text:
                x = 846 + letter * 57
                y = 40 + word * 77
                text_surface = font.render(character, True, (255, 255, 255))
                width, height = text_surface.get_width(), text_surface.get_height()
                screen.blit(text_surface, (x - width / 2, y - height / 2))
                letter += 1

            for i in range(12):
                if guesses[i] != '':
                    letter = 0
                    green, yellow = assess(guesses[i], answer)
                    for k in range(5):
                        x = 846 + letter * 57
                        y = 113 + i * 77
                        color_x = x - 26.5
                        color_y = y - 32.5
                        if green[k]:
                            pygame.draw.rect(screen, (1, 154, 1), (color_x, color_y, 53, 73))
                        if yellow[k]:
                            pygame.draw.rect(screen, (255, 196, 37), (color_x, color_y, 53, 73))
                        text_surface = font.render(guesses[i][k].lower(), True, (255, 255, 255))
                        size = font.size(guesses[i][k])
                        screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
                        letter += 1
            if guesses[11] != '' and guesses[11] != answer:
                text = 'L + Bozo'
                text_surface = font.render(text, True, (150, 0, 0))
                width = text_surface.get_width()
                screen.blit(text_surface, (480 - width / 2, 250))
                text_surface = font.render(answer, True, (255, 255, 255))
                width, height = text_surface.get_width(), text_surface.get_height()
                screen.blit(text_surface, (960 - width / 2, 40 - height / 2))
                reset = pygame.image.load('reset.png')
                screen.blit(reset, (352, 326))
                games += 1
                win_state = True

            for guess in guesses:
                if guess == answer:
                    text = 'You Win!'
                    text_surface = font.render(text, True, (255, 255, 255))
                    width = text_surface.get_width()
                    screen.blit(text_surface, (480 - width / 2, 326))
                    win_state = True
                    games += 1
                    correct += 1
                    with open('late_game_recognition_top_times', 'r+') as top_times:
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
                    open('late_game_recognition_top_times', 'w').close()
                    with open('late_game_recognition_top_times', 'w') as top_times:
                        top_times.writelines(content)

            end_time = pygame.time.get_ticks()
            counter = (end_time - start_time) / 1000
            timer_surface = font.render(str(round(counter, 2)), True, (255, 255, 255))
            width, height = timer_surface.get_width(), timer_surface.get_height()
            screen.blit(timer_surface, (430 - width / 2, 540 - height / 2))
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
                    if 25 < x < 112 and 25 < y < 69:
                        playing = False
                        win_state = False
                    if 352 < x < 608 and 326 < y < 454:
                        for i in range(12 - num):
                            starting_words.pop(num)
                        guesses = starting_words
                        screen.fill('BLACK')
                        screen.blit(background, (0, 0))
                        win_state = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.key.key_code(key):
                        for i in range(12 - num):
                            starting_words.pop(num)
                        guesses = starting_words
                        screen.fill('BLACK')
                        screen.blit(background, (0, 0))
                        win_state = False
            if go_back:
                playing = False
                win_state = False
            screen.blit(back_arrow, (25, 25))
            pygame.display.flip()
            clock.tick(60)
