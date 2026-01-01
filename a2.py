import turtle
screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(500, 500)
screen.title("Turtle Spiral")

polygon = turtle.Turtle()
side = 0

polygon.speed(0)

while True:
    #
    polygon.forward(side)
    polygon.left(60)
    
    side = side + 2