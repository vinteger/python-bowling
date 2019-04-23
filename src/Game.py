class Game:
    def __init__(self):
        self.current_score = 0

    def score(self):
        return self.current_score

    def roll(self, pins_knocked_down):
        self.current_score += pins_knocked_down
