paddleA : game.LedSprite = None
paddleB : game.LedSprite = None
paddleA = game.create_sprite(2, 4)
paddleB = game.create_sprite(3, 4)
ball = game.create_sprite(randint (0,4), 0)
directionY = 1
directionX = randint(0, 4)
basic.pause(200)

def on_button_pressed_a():
    if paddleA.get(Led LedSpriteProperty.X) > 0:
        paddleA.change(LedSpriteProperty.X, -1)
        paddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if paddleB.get(Led LedSpriteProperty.X) > 0:
        paddleA.change(LedSpriteProperty.X, 1)
        paddleB.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
