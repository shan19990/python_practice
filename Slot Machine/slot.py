import random
from collections import Counter

class Slot:
    
    def __init__(self, user):
        self.lines = user.line
        self.bet_amt = user.bet_amt
        self.each_line_bet = user.bet_amt / user.line
        self.winnings = 0
        self.slot_rows = 3
        
        
    def spin_slot(self):
        slot_odds = {'a':2,'b':3,'c':4,'d':5,'e':6}
        line = []
        winnings = 0
        keys_list = list(slot_odds.keys())
        for _ in range(self.lines) :
            for _ in range(self.slot_rows):
                line.append(random.choice(keys_list))
            counter = Counter(line)
            if len(counter) == 1:
                most_common_values = counter.most_common()
                most_common_value = most_common_values[0][0]
                winnings += slot_odds[most_common_value] * self.each_line_bet
            elif len(counter) == 2:
                most_common_values = counter.most_common()
                most_common_value = most_common_values[0][0]
                winnings += (slot_odds[most_common_value] * self.each_line_bet ) * 0.25
            else:
                winnings += 0
            print(line)
            line = []
        self.winnings = winnings
        
        return self.winnings