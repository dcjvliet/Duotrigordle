import pygame


def saveState():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    font = pygame.font.Font('Arial.ttf', 100)
    pygame.font.Font.set_underline(font, True)
    clock = pygame.time.Clock()
    broken = False
    back_arrow = pygame.image.load('back_arrow.png')
    use_config = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 25 < x < 112 and 25 < y < 69:
                    broken = True
                    break
                if 100 < x < 883 and 474 < y < 606:
                    use_config = True
                    broken = True
                    break
                if 1269 < x < 1820 and 474 < y < 606:
                    use_config = False
                    broken = True
                    break
        if broken:
            break
        text_surface = font.render('Load from config', True, (255, 255, 255))
        screen.blit(text_surface, (100, 474))
        text_surface = font.render('Create new', True, (255, 255, 255))
        screen.blit(text_surface, (1269, 474))
        screen.blit(back_arrow, (25, 25))
        pygame.display.flip()
        clock.tick(60)
    return use_config
