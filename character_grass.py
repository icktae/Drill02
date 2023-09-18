from pico2d import *

open_canvas()

# 오브젝트 생성
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 0, 90

# 사각이동 
while x < 770:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)


while y < 550:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(770, y)
    y = y + 2
    delay(0.01)

while x > 30:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 550)
    x = x - 2
    delay(0.01)

while y > 0:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(30, y)
    y = y - 2
    delay(0.01)


close_canvas()
