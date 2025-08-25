# Space Invaders – Python Turtle Edition
# ------------------------------------
# Controls: ← → to move, SPACE to shoot, Q to quit
# Goal: Shoot all aliens. Aliens drop closer every second. If they reach you, game over.
# Bunkers (barriers) absorb shots and alien contact.

import turtle as T
import random
import math

# --- Config ---
WIDTH, HEIGHT = 800, 600
MARGIN = 30
PLAYER_SPEED = 6
BULLET_SPEED = 12
ALIEN_HSTEP = 3            # horizontal speed per frame (changes sign at edges)
ALIEN_DROP_PIXELS = 18     # how many pixels they drop each wave
ALIEN_DROP_MS = 1000       # how often (ms) aliens drop closer to player
ALIEN_ROWS = 5
ALIEN_COLS = 10
ALIEN_SPACING_X = 60
ALIEN_SPACING_Y = 50
ALIEN_START_Y = 200
BULLET_COOLDOWN_MS = 250

# Bunker / barrier settings
BUNKER_COUNT = 3
BUNKER_BLOCKS_W = 7
BUNKER_BLOCKS_H = 4
BUNKER_BLOCK_SIZE = 12
BUNKER_Y = -120

# --- Screen setup ---
screen = T.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Space Invaders – Turtle")
screen.bgcolor("black")
screen.tracer(0)

# --- Drawing helpers ---


def make_turtle(shape='square', color='white', stretch=(1, 1), hidden=False):
    t = T.Turtle(visible=not hidden)
    t.speed(0)
    t.shape(shape)
    t.color(color)
    t.penup()
    t.shapesize(stretch[0], stretch[1])
    return t


# Register a simple triangle for the player
player_shape = ((0, -10), (10, 10), (-10, 10))
screen.register_shape('player_tri', player_shape)

# --- HUD ---
hud = make_turtle(hidden=True)
hud.color('white')
hud.goto(0, HEIGHT//2 - 40)

# --- Player ---
player = make_turtle('player_tri', '#46e1ff', (1.3, 1.3))
player.sety(-HEIGHT//2 + 70)
player_dx = 0
last_shot_time = 0

# --- Bullet ---
bullet = make_turtle('square', '#ffd447', (0.4, 1.2), hidden=True)
bullet_active = False

# --- Aliens ---
aliens = []
alien_direction = 1   # 1 -> right, -1 -> left

start_x = -((ALIEN_COLS-1) * ALIEN_SPACING_X)//2
for r in range(ALIEN_ROWS):
    for c in range(ALIEN_COLS):
        a = make_turtle('circle', '#7cff7c', (0.9, 0.9))
        a.goto(start_x + c*ALIEN_SPACING_X, ALIEN_START_Y - r*ALIEN_SPACING_Y)
        aliens.append(a)

# --- Bunkers ---
blocks = []


def create_bunker(center_x, base_y):
    # Create a rectangular bunker, with a small notch in the lower middle row
    for i in range(BUNKER_BLOCKS_H):
        for j in range(BUNKER_BLOCKS_W):
            # Add a notch: remove two center blocks on the bottom row
            if i == BUNKER_BLOCKS_H-1 and j in (BUNKER_BLOCKS_W//2 - 1, BUNKER_BLOCKS_W//2):
                continue
            b = make_turtle('square', '#9aa0a6',
                            (BUNKER_BLOCK_SIZE/20, BUNKER_BLOCK_SIZE/20))
            x = center_x + (j - (BUNKER_BLOCKS_W-1)/2) * \
                (BUNKER_BLOCK_SIZE + 2)
            y = base_y + (i - (BUNKER_BLOCKS_H-1)/2) * (BUNKER_BLOCK_SIZE + 2)
            b.goto(x, y)
            blocks.append(b)


# Place bunkers evenly spaced
bunker_spacing = WIDTH // (BUNKER_COUNT + 1)
for k in range(BUNKER_COUNT):
    cx = -WIDTH//2 + bunker_spacing*(k+1)
    create_bunker(cx, BUNKER_Y)

# --- Game state ---
score = 0
running = True

# --- Collisions ---


def hits(t1, t2, dist=18):
    return t1.distance(t2) < dist

# --- Controls ---


def move_left():
    global player_dx
    player_dx = -PLAYER_SPEED


def move_right():
    global player_dx
    player_dx = PLAYER_SPEED


def stop_move():
    global player_dx
    player_dx = 0


def fire():
    global bullet_active, last_shot_time
    if not running:
        return
    now = T.time()
    if bullet_active:
        return
    if (now - last_shot_time) * 1000 < BULLET_COOLDOWN_MS:
        return
    last_shot_time = now
    bullet_active = True
    bullet.goto(player.xcor(), player.ycor() + 20)
    bullet.showturtle()


def quit_game():
    global running
    running = False


screen.listen()
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')
screen.onkeyrelease(stop_move, 'Left')
screen.onkeyrelease(stop_move, 'Right')
screen.onkeypress(fire, 'space')
screen.onkeypress(quit_game, 'q')


def alien_drop():
    global running
    if not running:
        return
    for a in list(aliens):
        a.sety(a.ycor() - ALIEN_DROP_PIXELS)

    check_game_over()
    screen.ontimer(alien_drop, ALIEN_DROP_MS)


def write_hud(text):
    hud.clear()
    hud.write(text, align='center', font=('Courier', 16, 'normal'))


def end_screen(text):
    global running
    running = False
    banner = make_turtle(hidden=True)
    banner.color('white')
    banner.goto(0, 0)
    banner.write(text + "\nPress Q to quit.", align='center',
                 font=('Courier', 24, 'bold'))


def check_game_over():

    py = player.ycor()
    for a in aliens:
        if a.ycor() - 10 <= py + 10:
            end_screen('GAME OVER')
            return True
    return False


edge_left = -WIDTH//2 + MARGIN
edge_right = WIDTH//2 - MARGIN

screen.ontimer(alien_drop, ALIEN_DROP_MS)

frame = 0

while running:

    new_x = player.xcor() + player_dx
    if new_x < edge_left:
        new_x = edge_left
    if new_x > edge_right:
        new_x = edge_right
    player.setx(new_x)

    if aliens:
        min_x = min(a.xcor() for a in aliens)
        max_x = max(a.xcor() for a in aliens)
        if max_x + ALIEN_HSTEP*alien_direction > edge_right or min_x + ALIEN_HSTEP*alien_direction < edge_left:
            alien_direction *= -1
        for a in aliens:
            a.setx(a.xcor() + ALIEN_HSTEP*alien_direction)

    if bullet_active:
        bullet.sety(bullet.ycor() + BULLET_SPEED)

        if bullet.ycor() > HEIGHT//2 - 10:
            bullet.hideturtle()
            bullet_active = False
        else:

            for a in list(aliens):
                if hits(bullet, a, 18):
                    a.hideturtle()
                    aliens.remove(a)
                    bullet.hideturtle()
                    bullet_active = False
                    score += 10
                    break

            if bullet_active:
                for b in list(blocks):
                    if hits(bullet, b, 16):
                        b.hideturtle()
                        blocks.remove(b)
                        bullet.hideturtle()
                        bullet_active = False
                        break

    for a in list(aliens):
        for b in list(blocks):
            if hits(a, b, 18):
                b.hideturtle()
                blocks.remove(b)

        if hits(a, player, 20):
            end_screen('GAME OVER')
            break

    if running and not aliens:
        end_screen('YOU WIN!')

    write_hud(f"Score: {score}   Aliens left: {len(aliens)}")

    screen.update()
    frame += 1


T.done()
