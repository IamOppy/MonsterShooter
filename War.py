import pygame
from sys import exit
import os
from pygame import font
from pygame.constants import K_SPACE, KEYDOWN
from pygame.sprite import spritecollide
#" FIND A WAY TO SHOOT GUN FROM POSITION OF PLAYER"
pygame.init()
GAME_ACTIVE = True
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
NAME_OF_DISPLAY = pygame.display.set_caption("City Defender")
CLOCK = pygame.time.Clock()
FONT_ = pygame.font.Font(os.path.join(
    "Assets/FONT", "FutureMillennium Black.ttf"), 50)

# GROUND LIMIT = 540 FOR player


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
        self.x = 400
        self.y = 600
        self.image = self.player_idles_list[self.player_index]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.gravity = 0.75
        self.walk_speed = 2
        self.vel_y = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_SPACE] and self.rect.bottom >= 540:
            self.vel_y = -20
        if keys[pygame.K_d] and self.rect.bottom == 540:
            dx = self.walk_speed

        if keys[pygame.K_a]:
            dx = -self.walk_speed
        # update rect position
        self.vel_y += self.gravity
        dy += self.vel_y

        self.rect.x += dx
        self.rect.y += dy

    def apply_border(self):
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
        self.apply_border()
        self.animate_state()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        Slime_1 = pygame.image.load(os.path.join(
            "Assets/Monster1Frames", "SlimeF1.png"))
        Slime_2 = pygame.image.load(os.path.join(
            "Assets/Monster1Frames", "SlimeF2.png"))
        Slime_3 = pygame.image.load(os.path.join(
            "Assets/Monster1Frames", "SlimeF3.png"))
        Slime_4 = pygame.image.load(os.path.join(
            "Assets/Monster1Frames", "SlimeF4.png"))
        Slime_5 = pygame.image.load(os.path.join(
            "Assets/Monster1Frames", "SlimeF5.png"))
        Slime_6 = pygame.image.load(os.path.join(
            "Assets/Monster1Frames", "SlimeF6.png"))

        self.slime_1 = pygame.transform.scale(Slime_1, (200, 300))
        self.slime_2 = pygame.transform.scale(Slime_2, (200, 300))
        self.slime_3 = pygame.transform.scale(Slime_3, (200, 300))
        self.slime_4 = pygame.transform.scale(Slime_4, (200, 300))
        self.slime_5 = pygame.transform.scale(Slime_5, (200, 300))
        self.slime_6 = pygame.transform.scale(Slime_6, (200, 300))

        self.slimeFrames = [self.slime_1, self.slime_2,
                            self.slime_3, self.slime_4, self.slime_5, self.slime_6]
        self.slime_index = 0

        self.image = self.slimeFrames[self.slime_index]
        self.rect = self.image.get_rect(bottomright=(1000, 600))

    def animate_state(self):
        self.slime_index += 0.1
        if self.slime_index >= len(self.slimeFrames):
            self.slime_index = 0
        else:
            self.image = self.slimeFrames[int(self.slime_index)]

    def update(self):
        self.animate_state()
        self.rect.x -= 3
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            print('Destroyed')
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.speed = 10
        self.image = pygame.Surface((50, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.rect.midbottom = (pos_x, pos_y)

    def update(self):
        self.rect.x += 5


player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)  # finisheD HERE

enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# SURFACES
background_surface = pygame.image.load(
    os.path.join("Assets", "Background.png"))


def sprite_collision():
    pass


def draw_window():
    SCREEN.blit(background_surface, (0, 0))
    player_group.draw(SCREEN)
    player_group.update()
    enemy_group.draw(SCREEN)
    enemy_group.update()
    bullet_group.update()
    bullet_group.draw(SCREEN)


enemy_Spawn = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_Spawn, 4000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if GAME_ACTIVE:
            if event.type == enemy_Spawn:
                enemy_group.add(Enemy())
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet(player.rect.centerx, player.rect.centery)
                bullet_group.add(bullet)

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
