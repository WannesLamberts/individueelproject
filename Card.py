import pygame
class Card:
    def __init__(self,pos,value):
        self.value=value
        self.pos=pos
        self.image=pygame.image.load("assets/"+str(value)+".png")
        self.image=pygame.transform.scale(self.image,(self.image.get_width()*3,self.image.get_height()*3))
        self.rect=self.image.get_rect()
        self.rect.center=self.pos
    def draw(self,surface):
        self.rect.center=self.pos
        surface.blit(self.image,self.rect)
