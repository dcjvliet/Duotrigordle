import pygame


pygame.init()
keycode = pygame.key.key_code(']')
screen = pygame.display.set_mode((1920, 1080))
screen.fill('BLACK')
pygame.display.flip()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == keycode:
                pygame.quit()
            else:
                print('yay')
    pygame.display.flip()
    clock.tick(60)