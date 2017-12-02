"""
Versão otimizada: Uso de funções em codigos repetido.
Estudo do uso de classes. No caso a classe turtle.
Usamos varias instancias da classe turtle. instancia como brad e angie.

Podemos pensar em uma classe como uma planta de um edificio. E em seus objetos (Edificios criado a partir da planta)
como exemplos  ou instancias dessa planta.

"""

import turtle #Usando a classe turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
    draw_square(brad)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    #Create the turtle Angie - Draw a circle
    #angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)

    window.exitonclick()

draw_art()
