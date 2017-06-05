class Game(object):
    def __init__(self):
        self.score = 0
        self.last_roll = 0
        self.roll = 1
        self.bonus = 0
        self.next_turn_bonus = 0

    def record_roll(self, num_pins_knocked):
        self.score += ((self.bonus + 1) * num_pins_knocked)
        self.bonus = self.next_turn_bonus
        self.next_turn_bonus = 0
        print self.bonus, self.next_turn_bonus
        if self.roll >= 19:
            pass
        elif self.roll % 2 == 0 or self.roll == 20:
            spare = self.last_roll + num_pins_knocked

            if spare == 10:
                self.bonus += 1
        else:
            if num_pins_knocked == 10:
                self._manage_strike()
        self.last_roll = num_pins_knocked
        self.roll += 1

    def get_score(self):
        return self.score

    def _manage_strike(self):
        self.roll += 1
        self.bonus += 1
        self.next_turn_bonus += 1
