from sys import exit
import pygame

pygame.init()  # initializes pygame
screen = pygame.display.set_mode((800, 400))  # set window dimensions
pygame.display.set_caption("Morks Island")  # setting name of window
clock = pygame.time.Clock()  # creating a clock variable to control fps
font = pygame.font.Font("Pixeltype.ttf", 50)  # setting font
game_active = True
start_time = 0


# score settings
def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = font.render("Score: " + str(current_time // 1000), False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(100, 50))
    screen.blit(score_surf,score_rect)
    score_rect = score_surf.get_rect(center=(100,50))
    print(current_time)


# menu settings
home_surf = font.render("Pixel Runner",False,'Black')
home_rect = home_surf.get_rect(center=(400,100))
home_surf2 = font.render("Click space bar to play again!",False,'Black')
home_rect2 = home_surf2.get_rect(center=(400,300))
home_player_surf = pygame.image.load("Platformer Art Complete Pack/Base pack/Player/p1_front.png")
home_player_rect = home_player_surf.get_rect(center=(400,200))

# map settings
background_surf = pygame.image.load("Platformer Art Complete Pack/Mushroom expansion/Backgrounds/bg_shroom.png")
ground_surf = pygame.image.load("ground.png").convert_alpha()
ground_rect = ground_surf.get_rect(center=(0, 310))

# you died message
death_surf = font.render("YOU'RE DEAD", False, 'Black')  # false is for the anti aliasing field, it smooths edges
death_rect = death_surf.get_rect(center=(400, 100))

# enemies
slime_surf = pygame.image.load(
    "Platformer Art Complete Pack/Base pack/Enemies/slimeWalk1.png").convert_alpha()  # dont forget convert alpha, removes background black/white base
slime_rect = slime_surf.get_rect(midbottom=(600, 310))


# player
player_surf = pygame.image.load("Platformer Art Complete Pack/Base pack/Player/p3_jump.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(70, 310))
player_gravity = 0
death_rect = death_surf.get_rect(center=(100,100))


while True:
    for event in pygame.event.get():  # all possible events in pygame.event0
        if event.type == pygame.QUIT:  # constant synonymous with quitting window
            pygame.quit()  # opposite to pygame.init
            exit()  # imported from sys

        if game_active:  # first run game active is true
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 310:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 310:
                    player_gravity = -20
        else: #restarting game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True  # game active is false, so we need to restart it
                slime_rect.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        # display map
        screen.blit(background_surf, (0, 0))  # block image transfer (put one surface on another surface)
        screen.blit(ground_surf, (0, 310))
        display_score()

        # slime moving
        slime_rect.right -= 4
        if slime_rect.right < 0:
            slime_rect.left = 800
        screen.blit(slime_surf, slime_rect)


        # player moving
        player_gravity += 1
        player_rect.y += player_gravity
        screen.blit(player_surf, player_rect)
        if player_rect.bottom >= 310:
            player_rect.bottom = 310
            player_gravity = 0

        # game ends if slime is collided with
        if slime_rect.colliderect(player_rect):
            game_active = False
            screen.blit(death_surf, death_rect)

#     mouse_pos = pygame.mouse.get_pos() # mouse.get_pressed() is a listener for mouse buttons
    # checking for collision
        if player_rect.colliderect(slime_rect):
            screen.blit(death_surf,death_rect)
            pygame.display.update()

    else:
        screen.fill((95,92,188))
        screen.blit(home_surf,home_rect)
        screen.blit(home_player_surf,home_player_rect)
        screen.blit(home_surf2,home_rect2)

    pygame.display.update()
    clock.tick(60)  # sets frames per second ceiling at 60
