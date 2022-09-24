from sys import exit
import pygame

pygame.init()  # initializes pygame
screen = pygame.display.set_mode((800, 400))  # set window dimensions
pygame.display.set_caption("Morks Island")  # setting name of window
clock = pygame.time.Clock()  # creating a clock variable to control fps
font = pygame.font.Font("Pixeltype.ttf", 50)  # setting font
score = 0

# setting and text surfaces
background_surf = pygame.image.load("Platformer Art Complete Pack/Mushroom expansion/Backgrounds/bg_shroom.png")
ground_surf = pygame.image.load("ground.png")
death_surf = font.render("YOU'RE DEAD", False, 'Black')  # false is for the anti aliasing field, it smooths edges
score_surf = font.render("Score: " + str(score),False,'Black')

# character surfaces
slime_surf = pygame.image.load( "Platformer Art Complete Pack/Base pack/Enemies/slimeWalk1.png").convert_alpha()  # dont forget convert alpha, removes background black/white base
player_surf = pygame.image.load("Platformer Art Complete Pack/Base pack/Player/p3_jump.png").convert_alpha()

#  rects
player_rect = player_surf.get_rect(midbottom=(70, 310))
slime_rect = slime_surf.get_rect(midbottom=(600, 310))
score_rect = score_surf.get_rect(center=(100,50))

while True:
    for event in pygame.event.get():  # all possible events in pygame.event
        if event.type == pygame.QUIT:  # constant synonymous with quitting window
            pygame.quit()  # opposite to pygame.init
            exit()  # imported from sys

    screen.blit(background_surf, (0, 0))  # block image transfer (put one surface on another surface)
    screen.blit(ground_surf, (0, 310))
    screen.blit(score_surf,score_rect)

    screen.blit(player_surf, player_rect)

    slime_rect.right -= 4
    if slime_rect.right < 0:
        slime_rect.left = 800
    screen.blit(slime_surf, slime_rect)

    mouse_pos = pygame.mouse.get_pos() # mouse.get_pressed() is a listener for mouse buttons
    # checking for collision
    if player_rect.colliderect(slime_rect):
        score -= 1
        pygame.display.update()
    else:
        score += 1

    pygame.display.update()
    clock.tick(60)  # sets frames per second ceiling at 60
