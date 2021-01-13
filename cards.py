from random import shuffle

class Card(object):
    def __init__(self,rank,suit):
        """
        docstring
        """
        self.suit=suit
        self.rank=rank
        self.showing = True     #for testing set to True
    
    def __repr__(self):
        if self.showing:
            if 2<=self.rank<=10:
                return str(self.rank)+ " of " + self.suit 
            elif self.rank==11:
                return "Jack of " + self.suit 
            elif self.rank==12:
                return "Queen of " + self.suit 
            elif self.rank==13:
                return "King of " + self.suit
            elif self.rank==14:
                return "Ace of " + self.suit
        else:
            return 'Card' 

    def __lt__(self,other):
        return self.rank < other.rank

class Deck(object):
    def __init__(self):
        """
        docstring
        """
        self.cards=[]
        self.suits={'Spades':4,'Hearts':3,'Diamonds':2,'Clubs':1}
        self.buildDeck()

    def buildDeck(self):
        for suit in self.suits:
            for i in range(2,15):
                self.cards.append(Card(i,suit))
   
    
    def shuffleDeck(self):
        shuffle(self.cards)

    def printDeck(self):
        for card in self.cards:
            print(card)

    def pickACard(self):
        try:
            return self.cards.pop()
        except:
            print("Deck is Empty!")
            return -1

    def __len__(self):
        return len(self.cards)
    
    def __repr__(self):
        return str(self.cards)

deck = Deck()
