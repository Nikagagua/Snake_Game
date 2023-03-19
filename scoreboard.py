from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


def get_high_score():
    with open("data.txt", mode='r') as data:
        return int(data.readline())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()
