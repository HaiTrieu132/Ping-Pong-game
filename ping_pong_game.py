from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #For racket
        self.image = transform.scale(image.load(player_image), (40, 210))
        #For ball
        self.image2 = transform.scale(image.load(player_image), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def reset_a(self):
        window.blit(self.image2, (self.rect.x, self.rect.y))
window = display.set_mode((960, 720))
display.set_caption("Ping Pong Game")

#Background
background = transform.scale(image.load("background.png"), (960, 720))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 510:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 510:
            self.rect.y += self.speed
game = True
finish = False

clock = time.Clock()
FPS = 60

player_a = Player("racket.png", 35, 360, 3)
player_b = Player("racket.png", 880 , 360, 3)
ball = Player("ball.png", 480, 360, 3)
speed_x = randint(-5, 5)
speed_y = randint(-5, 5)

font.init()
font1 = font.Font(None, 35)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player_a.reset()
        player_b.reset()

        ball.reset_a()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 670 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_a, ball) or sprite.collide_rect(player_b, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            lose1 = font1.render("PLAYER 1 LOSES!", True, (180, 0, 0))
            window.blit(lose1, (240, 360))
        if ball.rect.x > 960:
            finish = True
            lose2 = font1.render("PLAYER 2 LOSES!", True, (180, 0,0))
            window.blit(lose2, (240, 360))
        player_a.update_left()
        player_b.update_right()
        clock.tick(FPS)
        display.update()

