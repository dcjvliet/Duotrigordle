import pygame


def setKeybind(index, key=']'):
    pygame.init()
    screen = pygame.display.set_mode()
    color = '#333333'
    screen.fill(color)
    pygame.display.flip()
    clock = pygame.time.Clock()
    font = pygame.font.Font('Arial.ttf', 100)
    small_font = pygame.font.Font('Arial.ttf', 80)
    back_arrow = pygame.image.load('back_arrow.png')
    user_text = key
    broken = False
    triggered = False
    input_color = '#555555'
    base = ['Visual Studio', 'PyCharm']
    ide_color = '#555555'
    ide = False
    index = int(index)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 25 < x < 112 and 25 < y < 69:
                    broken = True
                    break
                if 1296 < x < 1896 and 100 < y < 250:
                    triggered = True
                    user_text = ''
                    input_color = '#777777'
                if 1296 < x < 1896 and 381 < y < 531:
                    ide = True
                    ide_color = '#777777'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if triggered:
                        triggered = False
                        input_color = '#555555'
                        if user_text == '':
                            user_text = key
                    if ide:
                        ide = False
                        ide_color = '#555555'
                elif event.key == pygame.K_UP:
                    if ide:
                        if index % 2 == 0:
                            index += 1
                        else:
                            index -= 1
                elif len(user_text) == 0:
                    user_text += event.unicode
        pygame.draw.rect(screen, color, (0, 0, 1920, 1080))
        pygame.draw.rect(screen, input_color, (1296, 100, 600, 150))
        pygame.draw.rect(screen, ide_color, (1296, 381, 600, 150))
        screen.blit(back_arrow, (25, 25))
        text_surface = font.render('Reset Hotkey', True, (255, 255, 255))
        screen.blit(text_surface, (25, 100))
        text_surface = font.render('IDE', True, (255, 255, 255))
        screen.blit(text_surface, (257, 391))
        user_surface = font.render(user_text, True, (255, 255, 255))
        size = font.size(user_text)
        screen.blit(user_surface, (1596 - size[0] / 2, 165 - size[1] / 2))
        ide_surface = small_font.render(base[index], True, (255, 255, 255))
        width, height = ide_surface.get_width(), ide_surface.get_height()
        screen.blit(ide_surface, (1596 - width / 2, 456 - height / 2))
        if broken:
            break
        pygame.display.flip()
        clock.tick(60)
    return index, user_text
    
