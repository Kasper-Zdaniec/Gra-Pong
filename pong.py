import turtle
def create_window():
    window = turtle.Screen() #ekran
    window.title("Pong Akademia Kodu") #tytuł
    window.bgcolor("black") #kolor ekranu
    window.setup(width=800, height=600)
    window.tracer(0 ) # szybkość odświeżania
    return window
def create_paddle(x,y):
    paddle = turtle.Turtle() # tworzyy jeden element do rysowania
    paddle.speed(0) # ustawia prędkość na zero
    paddle.shape("square") # tworzy prostokąt
    paddle.color("white") # nadania białego
    paddle.shapesize(stretch_wid=5,stretch_len=1) # rozmiar ustawia
    paddle.penup() # nie ma śladów żółwika
    paddle.goto(x,y) #przesuwam do punktu x: 350, y: 0
    return paddle
def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.goto(0,0)
    ball.penup()
    return ball
window = create_window()
paddle_left = create_paddle(-350,0)
paddle_right = create_paddle(350,0)
ball = create_ball()
window.listen()
def paddle_left_change(distance):
    y = paddle_left.ycor()
    y+=distance # y = y+distance
    paddle_left.sety(y) # ustaw współrzędna y
def paddle_left_up():
    paddle_left_change(20)
def paddle_left_down():
    paddle_left_change(-20)
def paddle_right_change(distance):
    y = paddle_right.ycor()
    y+=distance # y = y+distance
    paddle_right.sety(y) # ustaw współrzędna y
def paddle_right_up():
    paddle_right_change(20)
def paddle_right_down():
    paddle_right_change(-20)
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")
ball.dx = 0.2
ball.dy = -0.2 
# Up , Down
while True:
    window.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # gdy zdobyta jest bramka 2 przypadki
    if ball.xcor() >390 or ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx = ball.dx*-1
    # odbijanie się piłki od krawędzi górnej i dolnej
    if ball.ycor()>290 or ball.ycor() <-290:
        ball.dy = ball.dy*-1 # zmniejszaliśmy to teraz zwiększamy
    # prawa paletka
    # pierwszy if sprawdzi czy to jest na linii paletki, a nie gola
    if ((ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() <
        paddle_right.ycor()+40 and ball.ycor() >paddle_right.ycor()-40)):
        ball.setx(340)
        ball.dx*=-1
    if ((ball.xcor() <-340 and ball.xcor() >-350) and (ball.ycor() <
        paddle_left.ycor()+40 and ball.ycor() >paddle_left.ycor()-40)):
        ball.setx(-340)
        ball.dx*=-1