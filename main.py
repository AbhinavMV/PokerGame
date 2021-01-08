from cards import deck,Card
from players import Player
from scores import PokerScore

deck.shuffleDeck()

playerData = []
name = 65
for player in range(4):
    hand = [deck.pickACard() for i in range(5)]
    playerData.append(Player(chr(name),hand))
    name=name+1

playScore = []    
for player in playerData:
    print(player.hand)
    playScore.append(PokerScore(player.hand).checkScore())

print(playScore)

# hand = [Card("King","Heart",13),Card("Queen","Heart",12),Card("Jack","Heart",11),Card(10,"Heart",10),Card(9,"Heart",9),Card("Ace","Heart",14)]
# hand = [Card(9,"Heart",9),Card(8,"Heart",8),Card(7,"Heart",7),Card(6,"Heart",6),Card(5,"Heart",5)]
# hand = [Card(4,"Club",4),Card(4,"Spade",4),Card(4,"Heart",4),Card(4,"Diamond",4),Card("King","Heart",13)]
# hand = [Card("Ace","Heart",14),Card("Ace","Spade",14),Card("Ace","Club",14),Card("King","Spade",13),Card("King","Heart",13)]
# hand = [Card("Ace","Spade",14),Card(10,"Spade",10),Card(7,"Spade",7),Card(6,"Spade",6),Card(2,"Spade",2)]
# hand = [Card(5,"Club",5),Card(4,"Diamond",4),Card(3,"Spade",3),Card(2,"Heart",2),Card("Ace","Heart",14)]
# hand = [Card("Ace","Heart",14),Card("Ace","Spade",14),Card("Ace","Club",14),Card("King","Spade",13),Card("Queen","Heart",12)]
# hand = [Card("Ace","Heart",14),Card("Ace","Spade",14),Card("King","Heart",13),Card("King","Spade",13),Card("Queen","Diamond",12)]
# hand = [Card("Ace","Heart",14),Card("Ace","Club",14),Card("King","Heart",13),Card("Queen","Spade",12),Card("Jack","Diamond",11)]
# hand = [Card("Ace","Heart",14),Card("King","Heart",13),Card("Queen","Diamond",12),Card("Jack","Club",11),Card(9,"Spade",9)]
