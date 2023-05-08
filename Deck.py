import random
from Card import Card
class Deck:
    def __init__(self):
        self.cards=[]
        for value in [11,12,13]:
            self.cards.append(Card((0,0),value))
    def printDeck(self):
        for x in self.cards:
            print("value: "+str(x.value))
    def shuffle(self):
        random.shuffle(self.cards)
    def drawCard(self,loc):
        card=self.cards.pop()
        card.pos=loc
        return card





