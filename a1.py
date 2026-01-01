import turtle

# Setup the screen
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500, 500)
turtle.Screen().title("Turtle")
polygon=turtle.Turtle()
side=8
length=100
angle=360/side
for i in range(side):
  polygon.forward(length)
  polygon.right(angle)
turtle.done()