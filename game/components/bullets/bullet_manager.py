import pygame
from game.components.bullets.bullet import Bullet
from game.components.spaceship import Spaceship
from game.utils.constants import ENEMY_TYPE


class BulletManager:
    def __init__(self, ):
        self.enemy_bullets = []


    def update(self, game):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets) 
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                game.score += 1
                game.playing = False
                game.death_count += 1
                print(game.death_count)
                pygame.time.delay(1000)
                break



    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)

    def add_bullets(self, spaceship):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))
    