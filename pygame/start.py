import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')

sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
test_surface = test_font.render("My Game",False ,'Black')
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("graphics/Player/player_stand.png")

snail_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(test_surface,(300,50))
    snail_x_pos -= 5
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,265))
    screen.blit(player_surface, (0, 265))
    pygame.display.update()
    clock.tick(60)