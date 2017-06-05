class Game(object):
    def __init__(self):
        self.score = 0

    def record_roll(self, num_pins_knocked):
        self.score += num_pins_knocked

    def get_score(self):
        return self.score
