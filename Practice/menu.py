import pygame
import recognition
import starting
import accuracy
import multitasking
import keybinds
import late_game
import top_times
import config_reader
import save_state


def mainMenu():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    font = pygame.font.Font('Arial.ttf', 80)
    small_font = pygame.font.Font('Arial.ttf', 55)
    big_font = pygame.font.Font('Arial.ttf', 120)
    clock = pygame.time.Clock()
    pygame.font.Font.set_underline(font, True)
    pygame.font.Font.set_underline(small_font, True)
    pygame.font.Font.set_underline(big_font, True)
    config = config_reader.configRead()
    try:
        filler = config[7]
        filled = True
    except IndexError:
        filled = False
    if filled:
        key = config[7][0]
        ide = int(config[7][1].split('\n')[0])
    else:
        key = ']'
        ide = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 25 < x < 794 and 25 < y < 131:
                    if filled:
                        use_config = save_state.saveState()
                        if not use_config:
                            num = recognition.numStartingWords()
                            starting_words = recognition.startingWords(num)
                            recognition.wordle(starting_words, num, key)
                            break
                        else:
                            starting_words = config[0]
                            num = config[1]
                            recognition.wordle(starting_words, num, key)
                            for i in range(6 - num):
                                config[0].pop(num)
                            for i in range(6 - num):
                                config[0].append('')
                            break
                    else:
                        num = recognition.numStartingWords()
                        starting_words = recognition.startingWords(num)
                        recognition.wordle(starting_words, num, key)
                        break
                elif 1271 < x < 1895 and 25 < y < 131:
                    if filled:
                        use_config = save_state.saveState()
                        if not use_config:
                            num = recognition.numStartingWords()
                            starting_words = recognition.startingWords(num)
                            starting.starting(starting_words, num, key)
                            break
                        else:
                            starting_words = config[2]
                            num = config[3]
                            starting.starting(starting_words, num, key)
                            for i in range(6 - num):
                                config[2].append('')
                            break
                    else:
                        num = recognition.numStartingWords()
                        starting_words = recognition.startingWords(num)
                        starting.starting(starting_words, num, key)
                        break
                elif 25 < x < 958 and 949 < y < 1055:
                    accuracy.blahblah()
                    break
                elif 1130 < x < 1895 and 949 < y < 1055:
                    if filled:
                        use_config = save_state.saveState()
                        if not use_config:
                            num = recognition.numStartingWords()
                            starting_words = recognition.startingWords(num)
                            multitasking.multitasking(starting_words)
                        else:
                            starting_words = config[4]
                            multitasking.multitasking(starting_words)
                    else:
                        num = recognition.numStartingWords()
                        starting_words = recognition.startingWords(num)
                        multitasking.multitasking(starting_words)
                elif 25 < x < 195 and 487 < y < 593:
                    pygame.quit()
                elif 1576 < x < 1895 and 487 < y < 593:
                    ide, key = keybinds.setKeybind(ide, key)
                elif 25 < x < 837 and 131 < y < 203:
                    if filled:
                        use_config = save_state.saveState()
                        if not use_config:
                            num = recognition.numStartingWords()
                            starting_words = recognition.startingWords(num)
                            late_game.lateGame(starting_words, num, key)
                        else:
                            starting_words = config[5]
                            num = config[6]
                            late_game.lateGame(starting_words, num, key)
                            for i in range(12 - num):
                                config[5].pop(num)
                            for i in range(6 - num):
                                config[5].append('')
                    else:
                        num = recognition.numStartingWords()
                        starting_words = recognition.startingWords(num)
                        late_game.lateGame(starting_words, num, key)
                elif 663 < x < 1257 and 462 < y < 618:
                    top_times.topTimes(ide)
                    break

        screen.fill(color)
        text_surface_1 = font.render('Recognition Practice', True, (255, 255, 255))
        screen.blit(text_surface_1, (25, 25))
        text_surface_2 = font.render('Starting Practice', True, (255, 255, 255))
        screen.blit(text_surface_2, (1271, 25))
        text_surface_3 = font.render('Typing Accuracy Practice', True, (255, 255, 255))
        screen.blit(text_surface_3, (25, 949))
        text_surface_4 = font.render('Multitasking Practice', True, (255, 255, 255))
        screen.blit(text_surface_4, (1130, 949))
        quit_surface = font.render('Quit', True, (255, 255, 255))
        height = quit_surface.get_height()
        screen.blit(quit_surface, (25, 540 - height / 2))
        info_surface = font.render('Settings', True, (255, 255, 255))
        width, height = info_surface.get_width(), info_surface.get_height()
        screen.blit(info_surface, (1895 - width, 540 - height / 2))
        text_surface_5 = small_font.render('Late Game Recognition Practice', True, (255, 255, 255))
        screen.blit(text_surface_5, (25, 131))
        text_surface_6 = big_font.render('Top Times', True, (255, 255, 255))
        screen.blit(text_surface_6, (663, 462))
        pygame.display.flip()
        clock.tick(60)


mainMenu()
