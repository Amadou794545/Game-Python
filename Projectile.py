import pygame


# classe qui gere la notion de projectile

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.originImage = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.originImage, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        # supprimer le projectile
        self.player.allProjectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        # verifier si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
            # supprimer le projectile
            self.remove()
