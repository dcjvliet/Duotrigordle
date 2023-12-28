import pygame


def starting(starting_words, num, key):
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
    word = 0
    guesses = [''] * num
    win_state = False
    playing = True
    go_back = False
    for i in range(6 - num):
        starting_words.pop(num)
    while playing:
        start_time = pygame.time.get_ticks()
        while not win_state:
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
                                word += 1
                        user_text = ''
                    elif event.key == pygame.key.key_code(key):
                        win_state = True
                        user_text = ''
                    elif len(user_text) < 5:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y= pygame.mouse.get_pos()
                    if 25 < x < 122 and 25 < y < 69:
                        go_back = True
                        win_state = True
            screen.blit(background, (0, 0))
            y = 700 - 95 * (5 - num)
            height = 95 + 95 * (5 - num)
            pygame.draw.rect(screen, '#333333', (772, y, 355, height))
            letter = 0

            for character in user_text:
                x = 809 + letter * 70
                y = 270 + word * 95
                text_surface = font.render(character.lower(), True, (255, 255, 255))
                size = font.size(character)
                screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
                letter += 1

            for i in range(num):
                if guesses[i] != '':
                    letter = 0
                    for character in guesses[i]:
                        x = 809 + letter * 70
                        y = 270 + i * 95
                        text_surface = font.render(character.lower(), True, (255, 255, 255))
                        size = font.size(character)
                        screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
                        letter += 1

            end_time = pygame.time.get_ticks()
            counter = (end_time - start_time) / 1000
            timer_surface = font.render(str(round(counter, 2)), True, (255, 255, 255))
            width, height = timer_surface.get_width(), timer_surface.get_height()
            screen.blit(timer_surface, (430 - width / 2, 540 - height / 2))
            back = pygame.image.load('back_arrow.png')
            screen.blit(back, (25, 25))
            if guesses[num - 1] != '':
                win_state = True
            pygame.display.flip()
        while win_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if 805 < x < 1061 and 925 < y < 1053:
                        screen.fill('BLACK')
                        screen.blit(background, (0, 0))
                        win_state = False
                        word = 0
                        if guesses == starting_words:
                            top_times.write(f'Time: {round(counter, 2)}\n')
                        guesses = [''] * num

                    if 25 < x < 112 and 25 < y < 69:
                        playing = False
                        win_state = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.key.key_code(key):
                        screen.fill('BLACK')
                        screen.blit(background, (0, 0))
                        win_state = False
                        word = 0
                        if guesses == starting_words:
                            with open('starting_times', 'r+') as top_times:
                                content = top_times.readlines()
                            open('starting_times', 'w').close()
                            with open('starting_times', 'w') as top_times:
                                content.append(f'Time: {round(counter, 2)}\n')
                                top_times.writelines(content)
                        guesses = [''] * num
            if go_back:
                playing = False
                win_state = False

            if guesses == starting_words:
                text_surface = font.render('Correct Words', True, (255, 255, 255))
                width = text_surface.get_width()
                screen.blit(text_surface, (960 - width / 2, 800))
            else:
                text_surface = font.render('Incorrect Words', True, (255, 255, 255))
                width = text_surface.get_width()
                screen.blit(text_surface, (960 - width / 2, 800))

            reset = pygame.image.load('reset.png')
            width = reset.get_width()
            screen.blit(reset, (960 - width / 2, 925))
            back = pygame.image.load('back_arrow.png')
            screen.blit(back, (25, 25))
            pygame.display.flip()
            clock.tick(60)
