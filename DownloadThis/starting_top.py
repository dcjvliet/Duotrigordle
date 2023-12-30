import pygame


def startingTop():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    color = '#333333'
    screen.fill(color)
    font = pygame.font.Font('Arial.ttf', 80)
    clock = pygame.time.Clock()
    pygame.display.flip()
    broken = False
    back_arrow = pygame.image.load('back_arrow.png')
    top_times = []
    times = []
    with open('starting_times', 'r') as best:
        content = best.readlines()
        for i in range(10):
            for line in content:
                parts = line.split(': ')
                parts = parts[1].split('\n')
                time = parts[0]
                if time not in top_times:
                    times.append(time)
            try:
                top_times.append(min(times))
            except ValueError:
                top_times.append('----')
            times = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 25 < x < 112 and 25 < y < 69:
                    broken = True
                    break
        if broken:
            break
        for i in range(10):
            y = 39 + i * 102
            text_surface = font.render(f'{str(i + 1)}.', True, (255, 255, 255))
            screen.blit(text_surface, (570, y))
        for i in range(10):
            y = 39 + i * 102
            text_surface = font.render(top_times[i], True, (255, 255, 255))
            width = text_surface.get_width()
            screen.blit(text_surface, (960 - width / 2, y))
        screen.blit(back_arrow, (25, 25))
        pygame.display.flip()
        clock.tick(60)

