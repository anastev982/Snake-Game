import pickle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.top_score = self.load_top_score()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 170)
        self.write(f"Score: {self.score}",
                   align="center",
                   font=("Arial", 16, "bold")
                   )
        self.goto(100, 170)
        self.write(f"Score: {self.top_score}",
                   align="center",
                   font=("Arial", 16, "bold")
                   )

    def load_top_score(self):
        try:
            with open("top_score.pkl", "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return 0

    def save_top_score(self):
        with open("top_score.pkl", "wb") as file:
            pickle.dump(self.top_score, file)

    def increase_score(self):
        self.score += 1
        if self.score > self.top_score:
            self.top_score = self.score
            self.save_top_score()
            self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "bold"))
