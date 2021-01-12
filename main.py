from cards import deck,Card
from players import Player
from scores import PokerScore
from collections import Counter
from hand import Hand

def compare(obj1,obj2):
    if obj1.handScore.score[1] > obj2.handScore.score[1]:
        return obj1,obj2
    elif obj1.handScore.score[1] < obj2.handScore.score[1]:
        return obj2,obj1
    else:
        hand1 = obj1.handScore.highestCard
        hand2 = obj2.handScore.highestCard
        score = obj1.handScore.score
        # To convert the sequence to 5 4 3 2 Ace 
        if hand1[0].rank==14 and hand1[-1].rank==2:
                a = hand1.pop(0)
                hand1.append(a)

        if hand2[0].rank==14 and hand2[-1].rank==2:
            a = hand2.pop(0)
            hand2.append(a)
            # print(hand2)
        #Royal Flush
        if score[1] == 10:
            return compareSuitOnly(obj1,obj2)
        #Straight Flush 
        if score[1] == 9:
            for i in range(len(hand1)):
                if hand1[i].rank == hand2[i].rank:
                    continue
                elif hand1[i].rank > hand2[i].rank:
                    return obj1,obj2
                else: 
                    return obj2,obj1
            return compareSuitOnly(obj1,obj2)
        # Rest of them 
        if 0<score[1]<9:
            return comparePairsValue(obj1,obj2)


def comparePairsValue(hand1,hand2):
    reducedList1 = sorted(Counter([i.rank for i in hand1.handScore.highestCard]).most_common(),key=lambda x: (x[1],x[0]),reverse=True)
    reducedList2 = sorted(Counter([i.rank for i in hand2.handScore.highestCard]).most_common(),key=lambda x: (x[1],x[0]),reverse=True)
    if reducedList1[0][0] == 14 and reducedList1[1][0]==5 and reducedList1[-1][0]==2 and reducedList1[0][1]==1:
        a = reducedList1.pop(0)
        reducedList1.append(a)
    if reducedList2[0][0] == 14 and reducedList2[1][0]==5 and reducedList2[-1][0]==2 and reducedList2[0][1]==1:
        a = reducedList2.pop(0)
        reducedList2.append(a)
    print(reducedList1,reducedList2)
    for i in range(0,len(reducedList1)):
        if reducedList1[i][0] == reducedList2[i][0]:
            continue
        elif reducedList1[i][0] > reducedList2[i][0]:
            return hand1,hand2
        elif reducedList1[i][0] < reducedList2[i][0]:
            return hand2,hand1
    return compareSuitOnly(hand1,hand2)

def compareSuitOnly(hand1,hand2):
    suits = {'Spades':4,'Hearts':3,'Diamonds':2,'Clubs':1}
    if suits[hand1.handScore.highestCard[0].suit] > suits[hand2.handScore.highestCard[0].suit]:
        return hand1,hand2
    return hand2,hand1

def sortDict(data):
    temp = data
    n = len(temp)
    for i in range(n):
        for j in range(i+1,n):
            temp[i],temp[j] = compare(temp[i],temp[j])         
    return temp

deck.shuffleDeck()

playerData = []
handName = []
name = 65
suit = {'s':'Spades','c':'Clubs','h':'Hearts','d':'Diamonds','j':11,'t':10,'k':13,'q':12,'a':14,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# card = [['ts','js','qs','ks','as'],['9s','9h','9d','9c','8s'],['8h','8d','8c','7s','7h'],['6s','6h','6d','5s','4s']]
# card = [['ts','js','qh','as','kh'],['3d','3s','3h','2h','2s'],['jc','qc','kc','7c','8c'],['2c','3c','4c','5c','6c']]
card = [['ah','3h','4h','9h','th'],['8h','8s','jh','jd','4c'],['2s','2d','2c','2h','3s'],['jc','js','5h','5c','3d']]
for player in card:
    h = []
    for i in player:
        h.append(Card(i[0],suit[i[1]],suit[i[0]]))
    playerData.append(Player(chr(name),h))
    name += 1
    # hand = [deck.pickACard() for i in range(5)]
    # playerData.append(Player(chr(name),hand))
    # name=name+1

for i in playerData:
    print(i,i.handScore,i.hand)
print(sortDict(playerData))
for i in playerData:
    print(i.handScore)




"""
All the hands for testing 
"""
# hande = PokerScore([Card("King","Hearts",13),Card("Queen","Hearts",12),Card("Jack","Hearts",11),Card(10,"Hearts",10),Card(9,"Hearts",9),Card("Ace","Hearts",14)])
# hand = PokerScore([Card("King","Spades",13),Card("Queen","Spades",12),Card("Jack","Spades",11),Card(10,"Spades",10),Card(9,"Spades",9),Card("Ace","Spades",14)])
# print(hand,hande)

# hande = PokerScore([Card("Ace","Hearts",14),Card(2,"Hearts",2),Card(3,"Hearts",3),Card(5,"Hearts",5),Card(4,"Hearts",4)])
# hand = PokerScore([Card("Ace","Spades",14),Card(2,"Spades",2),Card(3,"Spades",3),Card(5,"Spades",5),Card(4,"Spades",4)])

# h = PokerScore([Card(4,"Club",4),Card(4,"Spade",4),Card(4,"Heart",4),Card(4,"Diamond",4),Card("King","Heart",13)])
# hande = PokerScore([Card(5,"Club",5),Card(5,"Spade",5),Card(5,"Heart",5),Card(5,"Diamond",5),Card("King","Heart",13)])

# h = PokerScore([Card("Ace","Heart",14),Card("Ace","Spade",14),Card("Ace","Club",14),Card("King","Spade",13),Card("King","Heart",13)])
# hande = PokerScore([Card("Queen","Heart",12),Card("Queen","Spade",12),Card("Queen","Club",12),Card("King","Spade",13),Card("King","Heart",13)])

# a = compare(h,hande)
# print(a[0].highestCard,a[1].highestCard)



# h = PokerScore([Card("Ace","Spades",14),Card(10,"Spades",10),Card(7,"Spades",7),Card(6,"Spades",6),Card(2,"Spades",2)])
# hande = PokerScore([Card("Ace","Hearts",14),Card(10,"Hearts",10),Card(7,"Hearts",7),Card(6,"Hearts",6),Card(2,"Hearts",2)])

# h = PokerScore([Card(5,"Club",5),Card(4,"Diamond",4),Card(3,"Spade",3),Card(2,"Heart",2),Card("Ace","Heart",14)])
# hande = PokerScore([Card("Queen","Club",12),Card("Jack","Diamond",11),Card(10,"Spade",10),Card("King","Heart",13),Card("Ace","Spade",14)])


# h = PokerScore([Card("Ace","Heart",14),Card("Ace","Spade",14),Card("Ace","Club",14),Card("King","Spade",13),Card("Queen","Heart",12)])
# hande = PokerScore([Card("King","Heart",13),Card("King","Spade",13),Card("King","Club",13),Card("Ace","Diamond",14),Card("Queen","Heart",12)])

# hande =PokerScore([Card("Ace","Hearts",14),Card("Ace","Spades",14),Card("King","Hearts",13),Card("King","Spades",13),Card("Queen","Diamonds",12)])
# h = PokerScore([Card("Ace","Diamonds",14),Card("Ace","Clubs",14),Card("King","Diamonds",13),Card("King","Clubs",13),Card("Jack","Clubs",11)])

# hande = PokerScore([Card("Ace","Heart",14),Card("Ace","Club",14),Card("King","Heart",13),Card("Queen","Spade",12),Card(10,"Diamond",10)])
# h = PokerScore([Card("Ace","Diamond",14),Card("Ace","Spade",14),Card("King","Spade",13),Card("Jack","Spade",11),Card("Queen","Diamond",12)])

# hande = PokerScore([Card("Ace","Heart",14),Card("King","Heart",13),Card("Queen","Diamond",12),Card("Jack","Club",11),Card(9,"Spade",9)])
# h = PokerScore([Card("Ace","Diamond",14),Card("King","Spade",13),Card("Queen","Heart",12),Card(10,"Club",10),Card(9,"Spade",9)])



