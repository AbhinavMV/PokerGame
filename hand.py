from scores import PokerScore
class Hand(PokerScore):
    def __init__(self,cards):
        super().__init__(cards)
        
        self.values = [x.rank for x in self.cards]
        self.suits = [x.suit[0] for x in self.cards]



    def __repr__(self):
        return str(self.values)+str(self.suits)+str(self.score)
