import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets import bullet_manager

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = "left"
RIGHT = "right"



class Enemy(Sprite):
    X_POS_LIST = [i for i in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = random.randint (1, 4)
    SPEED_Y = 3
    def __init__(self):
        enemy_type = random.choice([ENEMY_1, ENEMY_2])
        self.image = pygame.transform.scale(enemy_type, (50, 50))
        self.type  = ENEMY_TYPE
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X

        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 100)
        self.moving_index = 0
        self.shooting_time = random.randint(30, 50)
        if enemy_type == ENEMY_2:
            self.speed_x  = random.randint (5,8)


    def update(self, enemies, bullet_manager):
        self.rect.y += self.speed_y
        self.shoot(bullet_manager)
        if self.movement == RIGHT:
           self.rect.x += self.speed_x
        else:
           self.rect.x -= self.speed_x

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)
    
    def update_movement(self):
        self.moving_index +=1
        if self.rect.right >= SCREEN_WIDTH:
           self.movement = LEFT
        elif self.rect.left <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet_manager.add_bullets(self)
            self.shooting_time += current_time + random.randint(30, 50)
        
    
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))        