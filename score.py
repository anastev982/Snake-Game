from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 170)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   align="center",
                   font=("Arial", 16, "bold")
                   )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "bold"))
