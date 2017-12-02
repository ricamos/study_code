import turtle #Usando a classe turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    mag = turtle.Turtle()
    mag.forward(100)
    mag.right(90)
    mag.forward(100)
    mag.right(135)
    mag.forward(142)


    window.exitonclick()

draw_square()