import pygame
class Button:
    def __init__(self,pos,image,action):
        self.action=action
        self.pos=pos
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.clicked=False
    def draw(self,surface):
        surface.blit(self.image,self.rect)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
                self.clicked=True
                return True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked=False
        return False