class Game(object):
    def __init__(self):
        self.score = 0
        self.pendant_strikes = 0

    def record_roll(self, num_pins_knocked):
        if self.pendant_strikes > 0:
            self.score += num_pins_knocked * self.pendant_strikes
            self.pendant_strikes -= 1
        self.score += num_pins_knocked
        if num_pins_knocked == 10:
            self.pendant_strikes += 1

    def get_score(self):
        return self.score
