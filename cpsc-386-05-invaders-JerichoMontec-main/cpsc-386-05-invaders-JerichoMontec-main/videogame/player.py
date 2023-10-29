import os
import pygame
from bullet import Bullet

class Player():
    def __init__(self, surface):
        self.name = "Player Ship"
        self.main_dir = os.path.dirname(__file__)
        self.data_dir = os.path.join(self.main_dir, "data")
        self.width = 48
        self.height = 48
        self.size = (self.width, self.height)
        self.x = 276
        self.y = 524 # Some constant value
        self.image = pygame.image.load(os.path.join(self.data_dir, "big_boss1.png"))
        self.rect = pygame.Rect((self.x, self.y), self.size)
        self.tick_speed = 3
        self.last_shot = pygame.time.get_ticks()
        self.shot_cooldown = 750
        self.bullet_list = []
        self.active = True
        self.invincible_buffer = pygame.time.get_ticks()
        self.invincible_cooldown = 3000
        self.flash_buffer = pygame.time.get_ticks()
        self.flash_cooldown = 250
        self.flash = True
        self.surface = surface
        self.surface.blit(self.image, self.rect)

    def update_rect(self):
        if self.active:
            self.rect = pygame.Rect((self.x, self.y), self.size)
        else:
            self.rect = pygame.Rect((0, 0), (1, 1))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= self.tick_speed
            if self.x < self.surface.get_rect().left + 20:
                self.x = self.surface.get_rect().left + 20
        elif key[pygame.K_RIGHT]:
            self.x += self.tick_speed
            if self.x > self.surface.get_rect().right - 20 - 48:
                self.x = self.surface.get_rect().right - 20 - 48
        self.update_rect()

    def draw(self):
        if self.flash:
            self.surface.blit(self.image, (self.x, self.y))

    def shoot(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            current = pygame.time.get_ticks()
            if current - self.last_shot >= self.shot_cooldown:
                self.last_shot = current
                new_bullet = Bullet(self.surface, ((self.x + self.width / 2 - 16), self.y - 16))
                self.bullet_list.append(new_bullet)
        for index, bullet in enumerate(self.bullet_list):
            if bullet.active is False:
                self.bullet_list.pop(index)

    def check_collision(self, bullet_list):
        if self.rect.collidelist(bullet_list) != -1:
            self.active = False
            bullet_list[self.rect.collidelist(bullet_list)].active = False
            return True
        return False
    
    def get_invincibility(self):
        self.invincible_buffer = pygame.time.get_ticks()

    def tangibility_buffer(self):
        current = pygame.time.get_ticks()
        if current - self.invincible_buffer >= self.invincible_cooldown:
            self.invincible_buffer = current
            return True
        return False

    def reset(self):
        self.x = 276
        self.y = 524
        self.update_rect()
        self.get_invincibility()

    def Flash(self, active):
        if active:
            self.flash = False
        else:
            self.flash = True

    def check_tangibility(self):
        if self.active is False and self.tangibility_buffer():
            self.active = True
            self.flash = True
            return False
        elif self.active is False:
            current = pygame.time.get_ticks()
            if current - self.flash_buffer >= self.flash_cooldown:
                self.flash_buffer = current
                self.Flash(self.flash)
        else:
            return True
