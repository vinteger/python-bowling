class Game:
    def __init__(self):
        self.rolls = []

    def score(self):
        total_score = 0
        roll_index = 0

        for frame_index in range(10):
            if self.__is_strike(roll_index):
                total_score += self.__strike_score(roll_index)
                roll_index += 1
            elif self.__is_spare(roll_index):
                total_score += self.__spare_score(roll_index)
                roll_index += 2
            else:
                total_score += self.__roll_frame(roll_index)
                roll_index += 2

        return total_score

    def roll(self, pins_knocked_down):
        self.rolls.append(pins_knocked_down)

    def __roll_frame(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]

    def __strike_score(self, roll_index):
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def __spare_score(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    def __is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def __is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
