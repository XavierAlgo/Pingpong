from pygame import *
color_bg = (255,255,255)
window = display.set_mode((750,500))
display.set_caption("Ping Pong")
window.fill(color_bg)

game = True
while game is True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()