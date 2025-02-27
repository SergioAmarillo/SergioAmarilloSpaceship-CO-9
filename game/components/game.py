from tkinter import Menu
import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies import enemy
from game.components.enemies.enemy_manager import EnemyManager

from game.components.spaceship import Spaceship
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        
        self.menu = Menu("press any key to start ...") 
        self.score = 0
        self.death_count = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.running:
            if not self.playing:
                self
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.playing = True
        self.enemy_manager.reset()
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.diplay.quit()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_close()

    def update(self):
        user_input = pygame
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self, font):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE)
        text = font.render(f"Score:{self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center(100, 50)
        self.screen.blit(text, text_rect)
      
    def show_menu(self):
        if self.death_count > 0:
            self.menu.update_message("other message")
        self.menuu.draw(self.screen)
        self.meu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False