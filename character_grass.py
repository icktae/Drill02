from pico2d import *
import math

open_canvas()

# 오브젝트 생성
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90
angle = 0

#반복
while(1):
    #사각이동
    while x < 770 :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 4
        delay(0.01)


    while y < 550 :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(770, y)
        y = y + 4
        delay(0.01)

    while x > 30 :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        x = x - 4
        delay(0.01)

    while y > 90 :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(30, y)
        y = y - 4
        delay(0.01)

    while x <400 :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 4
        delay(0.01)

    #원 이동
    while angle < 360 :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + math.cos(angle / 360 * 2 * math.pi) * 4
        y = y + math.sin(angle / 360 * 2 * math.pi) * 4
        angle = angle + 1
        delay(0.01)
        
     
close_canvas()
