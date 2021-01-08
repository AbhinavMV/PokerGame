from cards import Card
class PokerScore( object ):
    def __init__(self,hand):
        self.cards = hand
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

    def sameSuit(self):
        for card in range(len(self.cards)-4):
            for i in range(4):
                if self.cards[card+i].suit != self.cards[card+i+1].suit:
                    break
            else:
                return True
        return False

    def checkScore(self):
        if self.sameSuit():
            if self.straight():
                if self.cards[-1].rank==14 and self.cards[-5].rank==10:
                    return 10
                else:
                    return 9
            else:
                return 6
        elif self.straight():
            return 5
        else:
            return self.pairType()
        
    def straight(self):
        self.cards.sort()
        cd = [card.rank for card in self.cards]
        if self.cards[-1].rank==14 and self.cards[0].rank==2:
            for i in range(3):
                if self.cards[i].rank+1 != self.cards[i+1].rank:
                    return False
            return True
        if len(cd) == len(set(cd)):    
            for i in range(len(self.cards)-4):
                for j in range(4):
                    if self.cards[i+j].rank+1 != self.cards[i+j+1].rank:
                        break
                else:
                    return True
        return False

    def pairType(self):
        handCardCount = {}
        for card in self.cards:
            if card.rank not in handCardCount:
                handCardCount[card.rank] = 1
            else:
                handCardCount[card.rank] += 1

        vals = handCardCount.values()
        pairsCount = 0
        
        for i in vals:
            if i == 2:
                pairsCount+=1

        pairVal = max(vals)
        if pairVal==4:
            return 8
        elif pairVal==3 and pairsCount>=1:
            return 7
        elif pairVal==3:
            return 4
        elif pairVal==2 and pairsCount>=2:
            return 3
        elif pairVal==2:
            return 2
        else:
            return 1
