let paddleA : game.LedSprite = null
let paddleB : game.LedSprite = null
paddleA = game.createSprite(2, 4)
paddleB = game.createSprite(3, 4)
let ball = game.createSprite(randint(0, 4), 0)
let directionY = 1
let directionX = randint(0, 4)
basic.pause(200)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (paddleA.get(LedSpriteProperty.X) > 0) {
        paddleA.change(LedSpriteProperty.X, -1)
        paddleB.change(LedSpriteProperty.X, -1)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (paddleB.get(LedSpriteProperty.X) < 4) {
        paddleA.change(LedSpriteProperty.X, 1)
        paddleB.change(LedSpriteProperty.X, 1)
    }
    
})
basic.forever(function on_forever() {
    
    ball.change(LedSpriteProperty.X, directionX)
    ball.change(LedSpriteProperty.Y, directionY)
    pause(200)
})
