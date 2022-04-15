from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
MAX_SCORE_FONT = ('Courier', 16, 'normal')
GAME_OVER_FONT = ("Courier", 38, "bold")

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()
        self.max_score = 0

    def update_score(self):
        self.goto(0, 260)
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.new_score()
        self.load_max_score()
        self.goto(0,0)
        self.write('G A M E  O V E R !', align=ALIGNMENT, font=GAME_OVER_FONT)

        self.goto(0, -50)
        self.write(f'Max Score: {self.max_score}', align=ALIGNMENT, font=MAX_SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def load_max_score(self):
        with open('data/scores.txt', 'r') as f:
            score = f.read().strip()
        self.max_score = int(score)

    def new_score(self):
        with open('data/scores.txt', 'r') as f:
            score = int(f.read().strip())
        if self.score > score:
            with open('data/scores.txt', 'w') as f:
                f.write(str(self.score))