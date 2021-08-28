import turtle

window = turtle.Screen()
window.title("Pong by @balpbalpbalp")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

# Score

score_A = 0
score_B = 0

# Paddle A

paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B

paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Scoreboard

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: 0 - Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Function

def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

# Keyboard Binding

window.listen()
window.onkeypress(paddle_A_up, "w")
window.onkeypress(paddle_A_down, "s")
window.onkeypress(paddle_B_up, "Up")
window.onkeypress(paddle_B_down, "Down")

# Loop for the Game

while True:
    window.update()

    # Moving the Ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    # Top

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    # Bottom

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    # Left and Right

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {score_A} - Player B: {score_B}", align = "center", font = ("Courier", 24, "normal")) 

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {score_A} - Player B: {score_B}", align = "center", font = ("Courier", 24, "normal"))

    # Paddle and Ball Collision Scenarios

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
    
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1