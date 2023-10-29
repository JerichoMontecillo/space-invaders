import pygame
import os
from random import randint
from bullet import Bullet


direction = False
down = False

class Enemy:
    def __init__(self, surface, pos, choice):
        self.main_dir = os.path.dirname(__file__)
        self.data_dir = os.path.join(self.main_dir, "data")
        self.width = 32
        self.height = 32
        self.size = (self.width, self.height)
        self.x = pos[0]
        self.y = pos[1]
        self.image = self.get_image(choice)
        self.update_rect()
        self.tick_speed = 20
        self.last_move = pygame.time.get_ticks()
        self.move_buffer = 1000
        self.last_shot = pygame.time.get_ticks()
        self.shot_cooldown = randint(5000, 20000)
        self.bullet_list = []
        self.surface = surface
        self.active = True

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect((self.x, self.y), self.size)

    def get_image(self, choice):
        if choice == 0:
            return pygame.image.load(os.path.join(self.data_dir, "1_0.png"))
        elif choice == 1:
            return pygame.image.load(os.path.join(self.data_dir, "6_0.png"))
        elif choice == 2:
            return pygame.image.load(os.path.join(self.data_dir, "13.png"))

    def update_rect(self):
        self.rect = pygame.Rect((self.x, self.y), self.size)

    def move(self):
        global direction
        global down
        flag = 0
        if self.active and self.buffer_move():
            if direction:
                self.x = self.x + self.tick_speed
                if self.x > self.surface.get_rect().right - 20 - 32:
                    self.x = self.surface.get_rect().right - 30 - 32 - self.tick_speed
                    direction = False
                    flag = 1
            else:
                self.x = self.x - self.tick_speed
                if self.x < self.surface.get_rect().left + 20:
                    self.x = self.surface.get_rect().left + 30 + self.tick_speed
                    direction = True
                    flag = 1
        self.draw()
        return flag

    def smart_move(self):
        if self.active:
            if direction:
                self.x = self.x + (2 * self.tick_speed)
            else:
                self.x = self.x - (2 * self.tick_speed)
        self.draw()

    def smart_move_down(self):
        if self.active:
            if direction:
                self.x = self.x - self.tick_speed
            else:
                self.x = self.x + self.tick_speed
        self.draw()

    def move_down(self):
        if self.active and self.buffer_move():
            self.y = self.y + 25
        self.draw()

    def buffer_move(self):
        current = pygame.time.get_ticks()
        if current - self.last_move >= self.move_buffer:
            self.last_move = current
            return True
        return False


    def check_collision(self, bullet_list):
        if self.rect.collidelist(bullet_list) != -1:
            self.active = False
            bullet_list[self.rect.collidelist(bullet_list)].active = False
            return True
        else:
            return False

    def shoot(self):
        current = pygame.time.get_ticks()
        if current - self.last_shot >= self.shot_cooldown:
            self.last_shot = current
            new_bullet = Bullet(self.surface, ((self.x + self.width / 2 - 16), self.y + 32))
            self.bullet_list.append(new_bullet)
        for index, bullet in enumerate(self.bullet_list):
            if bullet.active is False:
                self.bullet_list.pop(index)
