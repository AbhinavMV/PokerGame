class Player(object):
    def __init__(self,name,cards):
        self.name = name
        for i in cards.hand:
            i.showing = True
        self.hand = cards
    
    def __repr__(self):
        return self.name

    # def __lt__(self,other):
    #     return self.handScore < other.handScore

