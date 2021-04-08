from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.scores=0
        self.hideturtle()
        self.write(f"Score ={self.scores} ", align="center", font=("Arial", 28, "normal"))



    def scoreadd(self):
        self.scores = self.scores+1
        self.clear()
        self.write(f"Score ={self.scores} ", align="center", font=("Arial", 28, "normal"))

    def gameouer(self):
        self.goto(0,0)
        self.write(f"Game Over ", align="center", font=("Arial", 28, "normal"))