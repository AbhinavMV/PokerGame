from random import shuffle

class Card(object):
    def __init__(self,value,suit,rank):
        """
        docstring
        """
        self.value=value
        self.suit=suit
        self.rank=rank

    def show(self):
        print(f"{self.value} of {self.suit}")

class Deck(object):
    def __init__(self):
        """
        docstring
        """
        self.cards=[]
        self.suits=['Spades','Hearts','Diamonds','Clubs']
        self.specialCards=['Jack','Queen','King','Ace']
        self.buildDeck()

    def buildDeck(self):
        for suit in self.suits:
            for i in range(2,11):
                self.cards.append(Card(i,suit,i))

            for j in self.specialCards:
                self.cards.append(Card(j,suit,i+1))
                i=i+1       
    
    def shuffleDeck(self):
        shuffle(self.cards)

    def printDeck(self):
        for card in self.cards:
            card.show()

    def pickACard(self):
        try:
            return self.cards.pop()
        except:
            print("Deck is Empty!")
            return -1

    def __len__(self):
        return len(self.cards)

d = Deck()
d.shuffleDeck()
d.printDeck()

    