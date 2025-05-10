import turtle

# Setup screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)

# Paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5, 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5, 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball movement variables
ball_dx = 0.2
ball_dy = 0.2

# Score
score_a = score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Movement functions
def move_paddle(paddle, y):
    if -240 < paddle.ycor() + y < 250:
        paddle.sety(paddle.ycor() + y)

# Key bindings
wn.listen()
wn.onkeypress(lambda: move_paddle(paddle_a, 20), "w")
wn.onkeypress(lambda: move_paddle(paddle_a, -20), "s")
wn.onkeypress(lambda: move_paddle(paddle_b, 20), "Up")
wn.onkeypress(lambda: move_paddle(paddle_b, -20), "Down")

# Main game
while True:
    wn.update()
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Border collision
    if abs(ball.ycor()) > 290:
        ball_dy *= -1

    # Scoring
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle collision
    if (ball.xcor() > 340 and abs(ball.ycor() - paddle_b.ycor()) < 50):
        ball.setx(340)
        ball_dx *= -1
    elif (ball.xcor() < -340 and abs(ball.ycor() - paddle_a.ycor()) < 50):
        ball.setx(-340)
        ball_dx *= -1