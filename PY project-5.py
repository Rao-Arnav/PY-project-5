import turtle

# SET UP THE DRAWING CANVAS
screen = turtle.Screen()
screen.title("Colour Loop Artwork")
screen.bgcolor("midnight blue")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# COLOUR LIST
colours = ["cyan", "orange", "hot pink", "yellow",
           "lime", "violet", "turquoise", "red"]

# FUNCTION TO DRAW ONE PETAL
def petal(colour):
    pen.fillcolor(colour)
    pen.begin_fill()

    pen.circle(70, 60)
    pen.left(120)
    pen.circle(70, 60)
    pen.left(120)

    pen.end_fill()

# DRAW THE OUTER FLOWER
for i in range(12):
    petal(colours[i % len(colours)])
    pen.left(30)

# DRAW A SMALLER FLOWER INSIDE
pen.penup()
pen.goto(0, 0)
pen.setheading(15)
pen.pendown()

for i in range(12):
    petal(colours[(i + 3) % len(colours)])
    pen.left(30)

# DRAW THE CENTRE CIRCLE
pen.penup()
pen.goto(0, -18)
pen.setheading(0)
pen.pendown()

pen.fillcolor("gold")
pen.begin_fill()
pen.circle(18)
pen.end_fill()

# FINISH
pen.hideturtle()
screen.exitonclick()