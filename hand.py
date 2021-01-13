from cards import Card
import itertools
class Hand(object):
    def __init__(self,cards):
        self.hand = cards
        self.values = [x.rank for x in self.hand]
        self.suits = [x.suit[0] for x in self.hand]
        self.score = self.evalHand()
        
    """
    lowest to highest - 
    High Card       - 1
    One pair        - 2
    Two Pair        - 3
    Three of a Kind - 4
    Straight        - 5
    Flush           - 6 
    Full House      - 7 
    Four of a Kind  - 8 
    Straight Flush  - 9
    Royal Flush     - 10
    """
    def evalHand(self):
        # Return ranking
        # 8. Straight Flush
        # 7. Four of a Kind
        # 6. Full House
        # 5. Flush
        # 4. Straight
        # 3. Three of a Kind
        # 2. Two pair
        # 1. One pair
        # 0. High card
        hand = sorted(self.hand,key=lambda x: x.rank,reverse=True)
        values = [c.rank for c in hand]
        suits = [c.suit for c in hand]
        # print(values,'\n'+str(suits))
        straight = (values == list(range(values[0], values[0]-5, -1))
                    or values == [14, 5, 4, 3, 2])
        flush = all(s == suits[0] for s in suits)

        if straight and flush: return 8,'Straight Flush'
        if flush: return 5,'Flush'
        if straight: return 4,'Straight'

        trips = []
        pairs = []
        for v, group in itertools.groupby(values):
            count = sum(1 for _ in group)
            if count == 4: return 7,'Four of a Kind'
            elif count == 3: trips.append(v)
            elif count == 2: pairs.append(v)

        if trips: return ((6,'Full House') if pairs else (3,'Three of a Kind'))
        l = len(pairs)
        if l==2: return 2,'Two Pair'
        if l==1: return 1,'One Pair'
        if l==0: return 0,'High Card'

    # def sameSuit(self):
    #     for card in range(len(self.hand)-4):
    #         for i in range(4):
    #             if self.hand[card+i].suit != self.hand[card+i+1].suit:
    #                 break
    #         else:
    #             return True
    #     return False

    # def checkScore(self):
    #     if self.sameSuit():
    #         if self.straight():
    #             if self.hand[-1].rank==14 and self.hand[-5].rank==10:
    #                 return 'Royal Flush',10
    #             else:
    #                 return 'Straight Flush',9
    #         else:
    #             return 'Flush',6
    #     elif self.straight():
    #         return 'Straight',5
    #     else:
    #         return self.pairType()
        
    # def straight(self):
    #     self.hand.sort()
    #     cd = [card.rank for card in self.hand]
    #     if self.hand[-1].rank==14 and self.hand[0].rank==2:
    #         for i in range(3):
    #             if self.hand[i].rank+1 != self.hand[i+1].rank:
    #                 return False
    #         return True
    #     if len(cd) == len(set(cd)):    
    #         for i in range(len(self.hand)-4):
    #             for j in range(4):
    #                 if self.hand[i+j].rank+1 != self.hand[i+j+1].rank:
    #                     break
    #             else:
    #                 return True
    #     return False

    # def pairType(self):
    #     handCardCount = {}
    #     for card in self.hand:
    #         if card.rank not in handCardCount:
    #             handCardCount[card.rank] = 1
    #         else:
    #             handCardCount[card.rank] += 1

    #     vals = handCardCount.values()
    #     pairsCount = 0
        
    #     for i in vals:
    #         if i == 2:
    #             pairsCount+=1
    #     pairVal = max(vals)
    #     if pairVal==4:
    #         return 'Four of a Kind',8
    #     elif pairVal==3 and pairsCount>=1:
    #         return 'Full House',7
    #     elif pairVal==3:
    #         return 'Three of a Kind',4
    #     elif pairVal==2 and pairsCount>=2:
    #         return 'Two Pair',3
    #     elif pairVal==2:
    #         return 'One Pair',2
    #     else:
    #         return 'High Card',1

    def compareTo(self,other):
        if self.score[0] > other.score[0]:
            return True
        elif self.score[0] < other.score[0]:
            return False
        from collections import Counter
        hand1CardCount = sorted(Counter([i.rank for i in self.hand]).most_common(),key=lambda x: (x[1],x[0]),reverse=True)
        hand2CardCount = sorted(Counter([i.rank for i in other.hand]).most_common(),key=lambda x: (x[1],x[0]),reverse=True)
        if hand1CardCount[0]==(14,1) and hand1CardCount[1]==(5,1) and hand1CardCount[-1]==(2,1):
            hand1CardCount.append(hand1CardCount.pop(0))
        if hand2CardCount[0]==(14,1) and hand2CardCount[1]==(5,1) and hand2CardCount[-1]==(2,1):
            hand2CardCount.append(hand2CardCount.pop(0))
        # print(hand1CardCount,hand2CardCount)
        for i in range(len(hand1CardCount)):
            if hand1CardCount[i] == hand2CardCount[i]:
                continue
            elif hand1CardCount[i][0] > hand2CardCount[i][0]:
                return True
            return False
        suits = {'Spades':4,'Hearts':3,'Diamonds':2,'Clubs':1} 
        for i in range(len(hand1CardCount)):
            if suits[self.hand[i].suit] == suits[other.hand[i].suit]:
                continue
            elif suits[self.hand[i].suit] > suits[other.hand[i].suit]:
                return True
            return False
        
    def __repr__(self):
        return "Score:"+ str(self.score) + "Hand:"+str(self.hand)

    def __lt__(self,other):
        return self.score<other.score



# e = Hand([Card(13,"Hearts"),Card(12,"Hearts"),Card(11,"Hearts"),Card(10,"Hearts"),Card(14,"Hearts")])

# e = Hand([Card(14,"Hearts"),Card(2,"Hearts"),Card(3,"Hearts"),Card(5,"Hearts"),Card(4,"Hearts")])

# e = Hand([Card(4,"Club"),Card(4,"Spade"),Card(4,"Heart"),Card(4,"Diamond"),Card(13,"Heart")])

# e1 = Hand([Card(14,"Hearts"),Card(14,"Spades"),Card(14,"Clubs"),Card(13,"Spades"),Card(13,"Hearts")])
# e1= Hand([Card(12,"Hearts"),Card(12,"Spades"),Card(12,"Clubs"),Card(13,"Diamonds"),Card(13,"Clubs")])
# print(e,e1)
# print(e.hand,e1.hand)
# print(e1.compareTo(e))