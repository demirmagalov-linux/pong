from ursina import *
import random
import time

app = Ursina()

paddle_right = Entity(model='quad', color=color.white, scale=(0.2, 1))
paddle_left = Entity(model='quad', color=color.white, scale=(0.2, 1))
ball = Entity(model='sphere', color=color.white, scale=(0.5, 0.5))

paddle_left.x = -7
paddle_right.x = 7
ball.x = 0
ball.speed_x = 5
ball.speed_y = 3
left_score = 0
right_score = 0
scoreboard = f"{left_score}:{right_score}"
score_text = Text(text=f'{scoreboard}', position=(0, 0.4), origin=(0, 0))
game_over = False

def update():
    global left_score, right_score, game_over
    if game_over:
        return
    score_text.text = f'{left_score} - {right_score}'   
    ball.x += ball.speed_x * time.dt
    ball.y += ball.speed_y * time.dt
    paddle_right.y += (ball.y - paddle_right.y) * 6.5 * time.dt
    if held_keys['w']:
        paddle_left.y += 0.05
    elif held_keys['s']:
        paddle_left.y -= 0.05    

    if ball.y > 4 or ball.y < -4:
        ball.speed_y = -ball.speed_y

    if ball.x >= 7 and paddle_right.y - 0.5 < ball.y < paddle_right.y + 0.5:
        ball.speed_x = -(abs(ball.speed_x) + 0.5)
        ball.x = 6.7
    elif ball.x <= -7 and paddle_left.y - 0.5 < ball.y < paddle_left.y + 0.5:
        ball.speed_x = abs(ball.speed_x) + 0.5
        ball.x = -6.7
    if ball.x > 8:
        left_score = left_score + 1
        if left_score == 5:
            Text(text='RIGHT SIDE WINS', position=(0, 0.2), origin=(0, 0))
            ball.speed_x = 0
            ball.speed_y = 0
            game_over = True
        ball.x = 0
        ball.y = 0
        ball.speed_x = random.choice([-1, 1]) * 5
        ball.speed_y = random.choice([-1, 1]) * 3
    if ball.x < -8:
        right_score = right_score + 1
        if right_score == 5:
            Text(text='LEFT SIDE WINS', position=(0, 0.2), origin=(0, 0))
            ball.speed_x = 0
            ball.speed_y = 0
            game_over = True
        ball.x = 0
        ball.y = 0
        ball.speed_x = random.choice([-1, 1]) * 5
        ball.speed_y = random.choice([-1, 1]) * 3
app.run()