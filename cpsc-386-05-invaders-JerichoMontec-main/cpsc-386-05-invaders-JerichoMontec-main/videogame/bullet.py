import os
import pygame

class Bullet:
    def __init__(self, surface, pos):
        self.main_dir = os.path.dirname(__file__)
        self.data_dir = os.path.join(self.main_dir, "data")
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.image.load(os.path.join(self.data_dir, "bullet_9.png"))
        self.flipped_image = pygame.transform.flip(self.image, False, True)
        self.rect = pygame.Rect((self.x, self.y), (32, 32))
        self.speed = 3
        self.active = True
        self.surface = surface
        self.surface.blit(self.image, self.rect)

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def update_rect(self):
        self.rect = pygame.Rect((self.x, self.y), (32, 32))

    def travel(self):
        if self.active:
            if self.y < self.surface.get_rect().top:
                self.active = False
            self.y = self.y - self.speed
            self.draw()
            self.update_rect()

    def enemy_travel(self):
        if self.active:
            if self.y > self.surface.get_rect().bottom:
                self.active = False
            self.y = self.y + self.speed
            self.enemy_draw()
            self.update_rect()

    def enemy_draw(self):
        self.surface.blit(self.flipped_image, (self.x, self.y))

    def check_collision(self, enemy_list):
        if self.rect.collidelist(enemy_list) != -1:
            self.active = False
            return True
        return False
