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
guesses = ['', '', '', '', '', '']
win_state = False

while True:
    with open('possible_answers') as possible_answers:
        content = possible_answers.readlines()
        randint = random.randint(0, 2309)
        answer = content[randint]
        parts = answer.split('\n')
        answer = parts[0]
        
    while not win_state:
        letter = 0
        
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
                            
                            for character in user_text:
                                x = 778 + letter * 70
                                y = 225 + word * 95
                                
                                if character in answer:
                                    rect = pygame.draw.rect(screen, (255, 196, 37), (x, y, 65, 90))
                                    
                                for i in range(5):
                                    if user_text[i] == answer[i]:
                                        rect = pygame.draw.rect(screen, (1, 154, 1), (x, y, 65, 90))
                                        
                                letter += 1
                            word += 1
                        user_text = ''
                        
                elif len(user_text) < 5:
                    user_text += event.unicode
                    
        screen.blit(background, (0, 0))

        for character in user_text:
            x = 809 + letter * 70
            y = 270 + word * 95
            color_x = x - 31
            color_y = y - 45
            text_surface = font.render(character.lower(), True, (255, 255, 255))
            size = font.size(character)
            screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
            letter += 1

        for i in range(6):
            if guesses[i] != '':
                
                letter = 0
                green, yellow = assess(guesses[i], answer)
                
                for k in range(5):
                    
                    x = 809 + letter * 70
                    y = 270 + i * 95
                    color_x = x - 31
                    color_y = y - 45
                    
                    if green[k]:
                        rect = pygame.draw.rect(screen, (1, 154, 1), (color_x, color_y, 65, 90))
                        
                    if yellow[k]:
                        rect = pygame.draw.rect(screen, (255, 196, 37), (color_x, color_y, 65, 90))
                        
                    text_surface = font.render(guesses[i][k].lower(), True, (255, 255, 255))
                    size = font.size(guesses[i][k])
                    screen.blit(text_surface, ((x - size[0] / 2), (y - size[1] / 2)))
                    letter += 1

        if guesses[5] != '' and guesses[5] != answer:
            text = 'You Lost!'
            text_surface = font.render(text, True, (150, 0, 0))
            width = text_surface.get_width()
            screen.blit(text_surface, (960 - width / 2, 850))
            reset = pygame.image.load('reset.png')
            screen.blit(reset, (805, 925))
            win_state = True

        for guess in guesses:
            if guess == answer:
                text = 'You Win!'
                text_surface = font.render(text, True, (255, 255, 255))
                width = text_surface.get_width()
                screen.blit(text_surface, (960 - width / 2, 850))
                win_state = True

        pygame.display.flip()
        clock.tick(60)
        
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
                    guesses = ['', '', '', '', '', '']
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    screen.fill('BLACK')
                    screen.blit(background, (0, 0))
                    win_state = False
                    word = 0
                    guesses = ['', '', '', '', '', '']
