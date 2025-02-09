import pygame
import random


def blahblah():
    pygame.init()
    color = '#333333'
    screen = pygame.display.set_mode((1920, 1080))
    screen.fill(color)
    pygame.display.flip()
    user_text = ''
    font = pygame.font.Font('Arial.ttf', 100)
    clock = pygame.time.Clock()
    broken = False
    win_state = False
    overall_start = pygame.time.get_ticks()
    words = 0
    while True:
        with open('possible_answers.txt', 'r') as possible:
            content = possible.readlines()
            randint = random.randint(0, 2309)
            line = content[randint]
            parts = line.split('\n')
            answer = parts[0]
        start_time = pygame.time.get_ticks()
        while not win_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            if user_text == answer:
                                win_state = True
                            else:
                                user_text = ''
                        else:
                            user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 25 < x < 112 and 25 < y < 69:
                        broken = True
            if broken:
                break
            pygame.draw.rect(screen, color, (0, 0, 1920, 1080))
            end_time = pygame.time.get_ticks()
            counter = (end_time - start_time) / 1000
            timer_surface = font.render(str(round(counter, 2)), True, (255, 255, 255))
            width, height = timer_surface.get_width(), timer_surface.get_height()
            screen.blit(timer_surface, (480 - width / 2, 540 - height / 2))
            try:
                wpm = words / ((end_time - overall_start) / 60000)
                wpm_surface = font.render(str(round(wpm, 2)), True, (255, 255, 255))
                width, height = wpm_surface.get_width(), wpm_surface.get_height()
                screen.blit(wpm_surface, (1440 - width / 2, 540 - height / 2))
            except ZeroDivisionError:
                wpm = 0
                wpm_surface = font.render(str(round(wpm, 2)), True, (255, 255, 255))
                width, height = wpm_surface.get_width(), wpm_surface.get_height()
                screen.blit(wpm_surface, (1440 - width / 2, 540 - height / 2))
            user_surface = font.render(user_text, True, (255, 255, 255))
            width, height = user_surface.get_width(), user_surface.get_height()
            screen.blit(user_surface, (960 - width / 2, 540 - height / 2))
            text_surface = font.render('WPM', True, (255, 255, 255))
            width, height = text_surface.get_width(), text_surface.get_height()
            screen.blit(text_surface, (1440 - width / 2, 440 - height / 2))
            back_arrow = pygame.image.load('back_arrow.png')
            screen.blit(back_arrow, (25, 25))
            answer_surface = font.render(answer, True, (255, 255, 255))
            width, height = answer_surface.get_width(), answer_surface.get_height()
            screen.blit(answer_surface, (960 - width / 2, 350 - height / 2))
            pygame.display.flip()
            clock.tick(60)
        while win_state:
            win_state = False
            user_text = ''
            words += 1
        if broken:
            break
