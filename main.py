import pygame
from pygame.constants import QUIT


pygame.init()

FPS = pygame.time.Clock()

HEIGH = 600
WIDTH = 1000

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGH))

player_size = (20, 20)

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]

playing = True

while playing:
    FPS.tick(240)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
   
    main_display.fill(COLOR_BLACK)
    
    if player_rect.bottom >= HEIGH:
        player_speed = [1, -1]
        player.fill((255, 0, 128))
    
    if player_rect.top <= 0:
        player_speed = [-1, 1]
        player.fill((255, 128, 18))
        
    if player_rect.right >= WIDTH:
        player_speed = [-1, -1]
        player.fill((0, 55, 213))
        
    if player_rect.left <= 0:
        player_speed = [1, 1]
        player.fill((140, 140, 114))
    
         
    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)
       
    pygame.display.flip()
   