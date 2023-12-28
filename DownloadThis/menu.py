import pygame
import recognition
import starting
import accuracy
import multitasking
import keybinds
import late_game
# ADD CONFIG FILE FOR STARTING, RECOGNITION, AND MULTITASKING
# ADD ACCESSIBLE WAY TO GET TOP TIMES

def mainMenu():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    font = pygame.font.Font('Arial.ttf', 80)
    small_font = pygame.font.Font('Arial.ttf', 55)
    clock = pygame.time.Clock()
    pygame.font.Font.set_underline(font, True)
    pygame.font.Font.set_underline(small_font, True)
    key = ']'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 25 < x < 794 and 25 < y < 131:
                    num = recognition.numStartingWords()
                    starting_words = recognition.startingWords(num)
                    recognition.wordle(starting_words, num, key)
                    break
                elif 1271 < x < 1895 and 25 < y < 131:
                    num = recognition.numStartingWords()
                    starting_words = recognition.startingWords(num)
                    starting.starting(starting_words, num, key)
                    break
                elif 25 < x < 958 and 949 < y < 1055:
                    accuracy.blahblah()
                    break
                elif 1130 < x < 1895 and 949 < y < 1055:
                    num = recognition.numStartingWords()
                    starting_words = recognition.startingWords(num)
                    multitasking.multitasking(starting_words)
                elif 25 < x < 195 and 487 < y < 593:
                    pygame.quit()
                elif 1576 < x < 1895 and 487 < y < 593:
                    key = keybinds.setKeybind(key)
                elif 25 < x < 837 and 131 < y < 203:
                    num = recognition.numStartingWords()
                    starting_words = recognition.startingWords(num)
                    late_game.lateGame(starting_words, num, key)

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
        pygame.display.flip()
        clock.tick(60)

mainMenu()
