import pygame

from Game import Game

pygame.init()
import Joueur



# Create the windows
screenName = pygame.display.set_caption("my Game")
screenDimension = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')
#charger le jeu
game = Game()

running = True

#boucle tant que la condition est vrai
while running:
    #appliquer l'arriere plan
    screenDimension.blit(background, (0, -200))
    #appliquer l'image du joueur
    screenDimension.blit(game.player.image, game.player.rect)

    for projectile in game.player.allProjectiles:
        projectile.move()

    #recuperer les projectiles du joueur
    game.player.allProjectiles.draw(screenDimension)
    print(game.pressed)
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screenDimension.get_width():
        game.player.moveRight()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.moveLeft()

    print(game.player.rect.x)
    #mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        #detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launchProjectile()

        #detecter si la touche espace est enclenchée pour lancer notre projectile
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False