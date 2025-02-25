import pygame
import webbrowser
import getpass
import starting_top


def topTimes(ide):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    font = pygame.font.Font('Arial.ttf', 120)
    pygame.font.Font.set_underline(font, True)
    clock = pygame.time.Clock()
    pygame.display.flip()
    broken = False
    user = getpass.getuser()
    back_arrow = pygame.image.load('back_arrow.png')
    recognition_vs = f'C:/Users/jacks/OneDrive/Desktop/Duotrigordle/DownloadThis/recognition_top_times.txt'
    recognition_pc = f'C:/Users/{user}/PycharmProjects/pythonProject/dcjvliet Duotrigordle main DownloadThis/recognition_top_times.txt'
    late_vs = f'C:/Users/jacks/OneDrive/Desktop/Duotrigordle/DownloadThis/late_game_recognition_top_times.txt'
    late_pc = f'C:/Users/{user}/PycharmProjects/pythonProject/dcjvliet Duotrigordle main DownloadThis/late_game_recognition_top_times.txt'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 642 < x < 1278 and 25 < y < 181:
                    if ide == 0:
                        print("recognition top times")
                        webbrowser.open(recognition_vs)
                    elif ide == 1:
                        webbrowser.open(recognition_pc)
                if 329 < x < 1591 and 462 < y < 618:
                    if ide == 0:
                        print("late game recognition top times")
                        webbrowser.open(late_vs)
                    elif ide == 1:
                        webbrowser.open(late_pc)
                if 25 < x < 112 and 25 < y < 69:
                    broken = True
                    break
                if 552 < x < 1368 and 899 < y < 1045:
                    starting_top.startingTop()
                    screen.fill(color)
        if broken:
            break
        text_surface = font.render('Recognition', True, (255, 255, 255))
        recognition_width = text_surface.get_width()
        screen.blit(text_surface, (960 - recognition_width / 2, 25))
        text_surface = font.render('Late Game Recognition', True, (255, 255, 255))
        late_width = text_surface.get_width()
        screen.blit(text_surface, (960 - late_width / 2, 462))
        text_surface = font.render('Starting Times', True, (255, 255, 255))
        width = text_surface.get_width()
        screen.blit(text_surface, (960 - width / 2, 899))
        screen.blit(back_arrow, (25, 25))
        pygame.display.flip()
        clock.tick(60)
        