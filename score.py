from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)

        self.write(f"Score :{self.x}",align='center', font=('Arial',8,'normal'))
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score :{self.x}", align='center', font=('Arial', 8, 'normal'))


    def increase(self):
        self.x += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center', font=('Arial', 8, 'normal'))

