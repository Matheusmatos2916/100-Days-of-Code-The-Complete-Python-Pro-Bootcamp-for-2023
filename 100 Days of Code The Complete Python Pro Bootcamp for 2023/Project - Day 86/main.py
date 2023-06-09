import turtle
 
# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
 
# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)
 
# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = -2.5
 
# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    for x in range(-7, 8):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(x * 60, 200 - y * 30)
        bricks.append(brick)
 
# Function to move the paddle left
def move_paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)
 
# Function to move the paddle right
def move_paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)
 
# Keyboard bindings
screen.listen()
screen.onkeypress(move_paddle_left, "Left")
screen.onkeypress(move_paddle_right, "Right")
 
# Main game loop
while True:
    screen.update()
 
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
 
    # Check for ball collision with walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
 
    # Check for ball collision with paddle
    if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1
 
    # Check for ball collision with bricks
    for brick in bricks:
        if (brick.xcor() - 30 < ball.xcor() < brick.xcor() + 30) and (brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10):
            ball.dy *= -1
            brick.goto(1000, 1000)
            bricks.remove(brick)
 
    # Check for game over
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        for brick in bricks:
            brick.goto(brick.xcor(), brick.ycor() - 50)
 
    # Check for game completion
    if len(bricks) == 0:
        paddle.goto(0, -250)
        ball.goto(0, 0)
        ball.dy *= -1
        for brick in bricks:
            brick.goto(brick.xcor(), brick.ycor() + 50)
        bricks = []
 
# Exit the game window
turtle.done()