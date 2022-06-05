from turtle import Screen

import pygame

# Initialise pygame
import running as running

pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('shoot spaceship.png')
playerX = 370
playerY = 480
playerX_change= 0

# Enemy
enemyImg = pygame.image.load('alien-3.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))
    
def enemy(x, y):
    screen.blit(enemyImg, (x, y))    

# Game Loop
running = True
while running:

    # Background Colour RGB = Red, Green, Blue
    screen.fill((153, 204, 255))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 - 5 + -0.1 -> 5 - 5 - 0.1
    # 5 - 5 + 0.1
    playerX += playerX_change
    
        if playerX <=0:
        playerX = 0
    elif playerX >= 756:
        playerX = 756
        
    # Enemy Movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 756:
        enemyX_change = -0.3
        enemyY += enemyY_change    
    
    
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
