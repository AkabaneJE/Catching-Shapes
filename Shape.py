import turtle


class Shape:
    def __init__(self, x, y, shapeType, color):
        self.shape = turtle.Turtle()
        self.shape.penup()
        self.shape.hideturtle()
        self.shape.speed(0)
        self.shape.goto(x, y)
        self.shape.color(color)
        self.shape.shape(shapeType)
        self.shape.shapesize(2, 2)

    def move(self):
        self.shape.sety(self.shape.ycor() - 20)

    def hide(self):
        self.shape.hideturtle()

    def show(self):
        self.shape.showturtle()
