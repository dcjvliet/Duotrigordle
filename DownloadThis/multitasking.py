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


def multitasking(starting_words):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    user_text = ''
    wordle = pygame.image.load('wordle_cropped.png')
    screen.blit(wordle, (403, 252))
    screen.blit(wordle, (1162, 252))
    font = pygame.font.Font(None, 110)
    clock = pygame.time.Clock()
    win_state = False
    color_in = False
    words = 0
    broken = False
    back_arrow = pygame.image.load('back_arrow.png')
    pygame.display.flip()
    with open('possible_answers') as possible:
        content = possible.readlines()
        randint = random.randint(0, 2309)
        answer_1 = content[randint]
        parts = answer_1.split('\n')
        answer_1 = parts[0]
    start_time = pygame.time.get_ticks()
    while True:
        with open('possible_answers') as possible:
            content = possible.readlines()
            randint = random.randint(0, 2309)
            answer_2 = content[randint]
            parts = answer_2.split('\n')
            answer_2 = parts[0]

        while not win_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]

                    elif event.key == pygame.K_RETURN:
                        if user_text == answer_1:
                            win_state = True
                            color_in = True
                            words += 1
                        else:
                            user_text = ''

                    elif len(user_text) < 5:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 25 < x < 112 and 25 < y < 69:
                        broken = True

            if broken:
                win_state = False
                break

            screen.fill(color)
            screen.blit(wordle, (403, 252))
            screen.blit(wordle, (1162, 252))
            screen.blit(back_arrow, (25, 25))
            letter = 0

            for character in user_text:
                x = 438 + letter * 70
                y = 774
                text_surface = font.render(character.lower(), True, (255, 255, 255))
                size = font.size(character)
                screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
                letter += 1

            if color_in:
                green, yellow = assess(user_text, answer_1)
                for i in range(5):

                    x = 438 + i * 70
                    y = 774
                    color_x = x - 30
                    color_y = y - 42

                    if green[i]:
                        pygame.draw.rect(screen, (1, 154, 1), (color_x, color_y, 65, 90))

                    if yellow[i]:
                        pygame.draw.rect(screen, (255, 196, 37), (color_x, color_y, 65, 90))

                    text_surface = font.render(user_text[i].lower(), True, (255, 255, 255))
                    size = font.size(user_text[i])
                    screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))

            for i in range(5):
                letter = 0
                green_1, yellow_1 = assess(starting_words[i], answer_1)
                green_2, yellow_2 = assess(starting_words[i], answer_2)

                for k in range(5):

                    x_1 = 438 + letter * 70
                    y = 299 + i * 95
                    x_2 = 1198 + letter * 70
                    color_x1 = x_1 - 30
                    color_x2 = x_2 - 30
                    color_y = y - 42

                    if green_1[k]:
                        pygame.draw.rect(screen, (1, 154, 1), (color_x1, color_y, 65, 90))

                    if yellow_1[k]:
                        pygame.draw.rect(screen, (255, 196, 37), (color_x1, color_y, 65, 90))

                    if green_2[k]:
                        pygame.draw.rect(screen, (1, 154, 1), (color_x2, color_y, 65, 90))

                    if yellow_2[k]:
                        pygame.draw.rect(screen, (255, 196, 37), (color_x2, color_y, 65, 90))

                    text_surface = font.render(starting_words[i][k].lower(), True, (255, 255, 255))
                    size = font.size(starting_words[i][k])
                    screen.blit(text_surface, ((x_1 - size[0] / 2), (y - size[1] / 2)))

                    text_surface = font.render(starting_words[i][k].lower(), True, (255, 255, 255))
                    size = font.size(starting_words[i][k])
                    screen.blit(text_surface, ((x_2 - size[0] / 2), (y - size[1] / 2)))
                    letter += 1

            end_time = pygame.time.get_ticks()
            total_time = (end_time - start_time) / 60000
            wpm = words / total_time
            wpm_surface = font.render(str(round(wpm, 2)), True, (255, 255, 255))
            width, height = wpm_surface.get_width(), wpm_surface.get_height()
            screen.blit(wpm_surface, (960 - width / 2, 540 - height / 2))
            label = font.render('WPM', True, (255, 255, 255))
            width, height = label.get_width(), label.get_height()
            screen.blit(label, (960 - width / 2, 440 - height / 2))
            pygame.display.flip()
            clock.tick(60)

        while win_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            user_text = ''
            answer_1 = answer_2
            color_in = False
            win_state = False
            pygame.time.wait(60)

        if broken:
            break
