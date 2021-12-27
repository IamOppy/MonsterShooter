import pygame
from sys import exit
import os
from pygame import font
from pygame.constants import K_SPACE, KEYDOWN
from pygame.sprite import spritecollide

pygame.init()
GAME_ACTIVE = True
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
NAME_OF_DISPLAY = pygame.display.set_caption("City Defender")
CLOCK = pygame.time.Clock()
FONT_ = pygame.font.Font(os.path.join(
    "Assets/FONT", "FutureMillennium Black.ttf"), 50)

# GROUND LIMIT = 540


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_idle_test_resize3 = pygame.image.load(
            os.path.join("Assets/Person1Frames", "Idle3.png")).convert_alpha()
        player_idle_test_resize2 = pygame.image.load(
            os.path.join("Assets/Person1Frames", "Idle2.png")).convert_alpha()
        player_idle_test_resize = pygame.image.load(
            os.path.join("Assets/Person1Frames", "Idle.png")).convert_alpha()
        player_Jump = pygame.image.load(
            os.path.join("Assets/Person1Frames", "JumpA.png")).convert_alpha()

        player_walk_1 = pygame.image.load(os.path.join(
            "Assets/Person1Frames/player_walk", "walk1.png")).convert_alpha()
        player_walk_2 = pygame.image.load(os.path.join(
            "Assets/Person1Frames/player_walk", "walk2.png")).convert_alpha()
        player_walk_3 = pygame.image.load(os.path.join(
            "Assets/Person1Frames/player_walk", "walk3.png")).convert_alpha()
        player_walk_4 = pygame.image.load(os.path.join(
            "Assets/Person1Frames/player_walk", "walk4.png")).convert_alpha()
        player_walk_5 = pygame.image.load(os.path.join(
            "Assets/Person1Frames/player_walk", "walk5.png")).convert_alpha()
        player_walk_6 = pygame.image.load(os.path.join(
            "Assets/Person1Frames/player_walk", "walk6.png")).convert_alpha()

        self.player_jump = pygame.transform.scale(player_Jump, (130, 140))
        self.player_idle_1 = pygame.transform.scale(
            player_idle_test_resize, (130, 140))
        self.player_idle_2 = pygame.transform.scale(
            player_idle_test_resize2, (130, 140))
        self.player_idle_3 = pygame.transform.scale(
            player_idle_test_resize3, (130, 140))

        self.player_walk_1 = pygame.transform.scale(player_walk_1, (130, 130))
        self.player_walk_2 = pygame.transform.scale(player_walk_2, (130, 130))
        self.player_walk_3 = pygame.transform.scale(player_walk_3, (130, 130))
        self.player_walk_4 = pygame.transform.scale(player_walk_4, (130, 130))
        self.player_walk_5 = pygame.transform.scale(player_walk_5, (130, 130))
        self.player_walk_6 = pygame.transform.scale(player_walk_6, (130, 130))

        self.player_idles_list = [self.player_idle_1,
                                  self.player_idle_2, self.player_idle_3]
        self.player_walk_list = [self.player_walk_1, self.player_walk_2,
                                 self.player_walk_3, self.player_walk_4, self.player_walk_5, self.player_walk_6]
        self.player_index = 0
        self.player_walk_index = 0

        self.image = self.player_idles_list[self.player_index]
        self.rect = self.image.get_rect(midbottom=(400, 540))
        self.gravity = 0
        self.walk_steps = 4

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 540:
            self.gravity -= 30
        if keys[pygame.K_d] and self.rect.bottom == 540:
            self.rect.x += self.walk_steps

        if keys[pygame.K_a]:
            self.rect.x -= self.walk_steps

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 540:
            self.rect.bottom = 540

    def animate_state(self):
        keys = pygame.key.get_pressed()
      # "FIND HOW TO CONTROL IF PLAYER WALKING STOP ANIMATION"
        if self.rect.bottom < 540:
            self.image = self.player_jump

        if keys[pygame.K_d] or keys[pygame.K_a]:
            self.player_walk_index += 0.1
            if self.player_walk_index >= len(self.player_walk_list):
                self.player_walk_index = 0
            self.image = self.player_walk_list[int(self.player_walk_index)]

        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_idles_list):
                self.player_index = 0
            self.image = self.player_idles_list[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate_state()


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pass


player = pygame.sprite.Group()
player.add(Player())


# SURFACES
background_surface = pygame.image.load(
    os.path.join("Assets", "Background.png"))


def draw_window():
    SCREEN.blit(background_surface, (0, 0))
    player.draw(SCREEN)
    player.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if GAME_ACTIVE:
            pass
        else:
            """Check for input to restart game ex. Reset time, Reset Enemy Position"""
            pass
    if GAME_ACTIVE:
        """DRAW WINDOW"""
        draw_window()

    else:
        """ALTERNATE BETWEEN SCREENS IF SCORE IS < 0 == START SCREEN OR IF SCORE > 0 == SHOW SCORE"""
        pass
    pygame.display.update()
    CLOCK.tick(60)
