paddleA : game.LedSprite = None
paddleB : game.LedSprite = None
paddleA = game.create_sprite(2, 4)
paddleB = game.create_sprite(3, 4)
ball = game.create_sprite(randint (0,4), 0)
directionY = 1
directionX = randint(0, 4)
basic.pause(200)

def on_button_pressed_a():
    if paddleA.get(LedSpriteProperty.X) > 0:
        paddleA.change(LedSpriteProperty.X, -1)
        paddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if paddleB.get(LedSpriteProperty.X) < 4:
        paddleA.change(LedSpriteProperty.X, 1)
        paddleB.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global directionX , directionY
    ball.change(LedSpriteProperty.X,directionX)
    ball.change(LedSpriteProperty.Y,directionY)
    pause(200)
    if ball.is_touching(paddleA):
        ball.change(LedSpriteProperty.Y, -1)
        directionY = -1
        directionX = randint(-1, 1)
    elif ball.get(LedSpriteProperty.Y) >= 4:
        ball.set(LedSpriteProperty.BLINK, 0)
        basic.pause(2000)
        game.game_over()
    if ball.get(LedSpriteProperty.X) <= 0:
        directionX = 1
    elif ball.get(LedSpriteProperty.X) >= 4:
        directionX = -1
    basic.pause(100)
basic.forever(on_forever)
