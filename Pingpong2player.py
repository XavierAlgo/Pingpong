from pygame import *
from random import randint
from time import sleep



color_bg = (255,255,255)
window = display.set_mode((750,500))
display.set_caption("Ping Pong")
bg = transform.scale(image.load('court.webp'), (700, 500))
#FPS
fps = time.Clock()




class GameSprite(sprite.Sprite):
    def __init__ (self,img,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.x = x
        self.y = y
        self.speed = speed                    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))            


class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.x < (700-75):
               self.rect.x += self.speed
        if key_pressed[K_s] and self.rect.x > 5 :
             self.rect.x -= self.speed


class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.x < (700-75):
               self.rect.x += self.speed
        if key_pressed[K_DOWN] and self.rect.x > 5 :
             self.rect.x -= self.speed



p1 = Player1('leftracket.png',375,250,100,100,3)


game = True
while game is True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    fps.tick(60)
    p1.reset()
    p1.update()
    display.update()