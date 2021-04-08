from turtle import Turtle



class Snake:
    def __init__(self):
        self.pos = 0
        self.segments = []
        for i in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(self.pos, 0)
            self.pos = self.pos - 20
            self.segments.append(square)



    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            pos_x = self.segments[seg - 1].xcor()
            pos_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(pos_x, pos_y)
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)


    def down(self):
        self.segments[0].setheading(270)


    def right(self):
        self.segments[0].setheading(0)


    def left(self):
        self.segments[0].setheading(180)

    def addsegment(self):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(self.pos, 0)
        self.pos = self.pos - 20
        self.segments.append(square)

    def collide(self):
                return False


