import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("Light blue")
screen.title("Turtle Oyunu")
screen.setup(width=800, height=600)

kaplumbağa = turtle.Turtle()
kaplumbağa.shape("turtle")
kaplumbağa.turtlesize(2, 2)
kaplumbağa.penup()

skor = 0
süreLimiti = 30

skorGörünüş = turtle.Turtle()
skorGörünüş.hideturtle()
skorGörünüş.penup()
skorGörünüş.goto(-370, 260)
skorGörünüş.write(f"Skor: {skor}", align="left", font=("Arial", 16, "normal"))


sayaç = turtle.Turtle()
sayaç.hideturtle()
sayaç.penup()
sayaç.goto(270, 260)
sayaç.write("Time Left: 30", align="left", font=("Arial", 16, "normal"))




def move_turtle(x, y):
    global skor
    kaplumbağa.hideturtle()
    yeniX = random.randint(-390, 390)
    yeniY = random.randint(-290, 290)
    kaplumbağa.goto(yeniX, yeniY)
    kaplumbağa.showturtle()


    skor += 1
    skorGörünüş.clear()
    skorGörünüş.write(f"Skor: {skor}", align="left", font=("Arial", 16, "normal"))


kaplumbağa.onclick(move_turtle)

def geriSayım(kalanSüre):
    if kalanSüre > 0:
        sayaç.clear()
        sayaç.write(f"Time Left: {kalanSüre}", align="left", font=("Arial", 16, "normal"))
        screen.ontimer(lambda: geriSayım(kalanSüre - 1), 1000)
    else:
        kaplumbağa.hideturtle()
        screen.title(f"Oyun Bitti! Son Skor: {skor}")

geriSayım(süreLimiti)

screen.mainloop()
