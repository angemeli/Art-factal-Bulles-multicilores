import pygame
import random

pygame.init()

#Paramétrage de la fenêtre
screen_width, screen_height = (1600,837)
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Factal")

clock = pygame.time.Clock()

#Chargement des audios
back_sound = pygame.mixer.Sound("bg002.mp3")
back_sound.set_volume(0.6)
back_sound.play(50, 0, 2500)
sound = pygame.mixer.Sound("coin.wav")

#Liste stockant les différents cercles
balls = []

for _ in range(15) :
    #Création des bulles
    balls.append({
        'pos': [random.randint(100,1400), random.randint(100,600)],
        'size': 100,
        'color': (random.randint(0,255), random.randint(0,255), random.randint(0,255)),
        'velocity': [random.choice([-1,1]), random.choice([-1,1])],
    })

noir = (0,0,0)

running = True

#Boucle principale
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(noir)

    #Dessin des balles et des déplacements
    for ball in balls :
        pygame.draw.circle(screen, ball['color'], (ball['pos'][0], ball['pos'][1]), ball['size'], 10)
        ball['color'] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ball['pos'][0] += ball['velocity'][0]
        ball['pos'][1] += ball['velocity'][1]
        
        #Gérer les collisions avec les bords de la fenêtre
        if (ball['pos'][0] < ball['size']) or ((ball['pos'][0] + ball['size']) > screen_width) :
            sound.play(0, 500)
            ball['velocity'][0] *= -1
        if (ball['pos'][1] < ball['size']) or ((ball['pos'][1] + ball['size']) > screen_height) :
            sound.play(0, 500)
            ball['velocity'][1] *= -1
    
    pygame.display.flip()
    clock.tick(100)


pygame.quit()