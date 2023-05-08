import pygame
from Card import *
from Deck import *
from Button import *
pygame.init()
surface=pygame.display.set_mode((1366,768))
surface.fill((77,136,213))
pygame.display.set_caption("pokerAI")
checkButtonImg = pygame.image.load('assets/green.png').convert_alpha()
callButtonImg = pygame.image.load('assets/blue.png').convert_alpha()
raiseButtonImg = pygame.image.load('assets/yellow.png').convert_alpha()
foldButtonImg = pygame.image.load('assets/red.png').convert_alpha()
clock=pygame.time.Clock()

class gameKuhn:
    def __init__(self):
        self.drawableObjects=[]
    def drawText(self,text,pos):
        font = pygame.font.SysFont("Arial", 24)
        img=font.render(text,True,(0,0,0))
        surface.blit(img,pos)
    def clickedButtons(self,actions,buttons):
        for action in actions:
            if action == "b" and buttons[0].draw(surface):
                return "b"
            elif action == "c" and buttons[1].draw(surface):
                return "c"
            elif action == "r" and buttons[2].draw(surface):
                return "r"
            elif action == "f" and buttons[3].draw(surface):
                return "f"
    def winner(self,cardP1,cardP2,pot,chipsp1,chipsp2):
        if cardP1.value > cardP2.value:
             chipsp1+=pot
        else:
             chipsp2+=pot
        return chipsp1,chipsp2
    def play(self):
        callButton=Button((330,600),callButtonImg,"b")
        checkButton=Button((250,600),checkButtonImg,"c")
        raiseButton=Button((170,600),raiseButtonImg,"r")
        foldButton=Button((90,600),foldButtonImg,"f")
        nextRoundButton=Button((1100,600),foldButtonImg,"n")
        finished=False
        history=""
        pot=0
        p1Chips=3
        p2Chips=3
        while not finished:
            clock.tick(60)
            surface.fill((77, 136, 213))
            self.drawText("p1 chips "+str(p1Chips), (740, 500))
            self.drawText("p2 chips "+str(p2Chips), (740, 200))
            self.drawText(str(pot), (640, 330))
            #if((p1Chips==0 or p2Chips==0) and history==""):
                #surface.fill((77, 136, 213))
                #self.drawText("GAME OVER", (740, 200))
                #continue
            if history=="":
                deck=Deck()
                deck.shuffle()
                p1Card=deck.drawCard((660,500))
                p2Card=deck.drawCard((660,200))
                pot=0
                p1Chips-=1
                p2Chips-=1
                pot=pot+2
                history+="s"
            if history=="F":
                self.drawText("ROUND OVER ", (100, 60))
                if nextRoundButton.draw(surface):
                    history=""
            p1Card.draw(surface)
            p2Card.draw(surface)
            if len(history)%2==1:
                self.drawText("PLAYER1 TURN ", (100, 300))
                if history=="s":
                    if checkButton.draw(surface):
                        history+="c"
                    elif raiseButton.draw(surface):
                        pot+=1
                        p1Chips-=1
                        history+="r"
                if history=="scr":
                    if callButton.draw(surface):
                        p1Chips-=1
                        p1Chips,p2Chips=self.winner(p1Card,p2Card,pot,p1Chips,p2Chips)
                        history="F"
                    elif foldButton.draw(surface):
                        p2Chips+=pot
                        history="F"
            else:
                self.drawText("PLAYER2 TURN ", (100, 300))
                if history=="sr":
                    if callButton.draw(surface):
                        p2Chips-=1
                        pot+=1
                        p1Chips,p2Chips=self.winner(p1Card,p2Card,pot,p1Chips,p2Chips)
                        history="F"
                    elif foldButton.draw(surface):
                        p1Chips+=pot
                        history="F"
                if history=="sc":
                    if checkButton.draw(surface):
                        p1Chips,p2Chips=self.winner(p1Card,p2Card,pot,p1Chips,p2Chips)
                        history="F"
                    elif raiseButton.draw(surface):
                        p2Chips-=1
                        pot+=1
                        history+="r"
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished=True
