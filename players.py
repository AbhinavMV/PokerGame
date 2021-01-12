from scores import PokerScore
class Player(object):
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
        self.handScore = PokerScore(hand)
    
    def __repr__(self):
        return self.name

    def __lt__(self,other):
        return self.hand < other.hand

