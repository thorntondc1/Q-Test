import pygame
import os
from pygame.locals import *
import random, urllib.request
from bs4 import BeautifulSoup

pygame.font.init()


WIDTH = 800
HEIGHT = 600

BLACK = (0,0,0)
GRAY = (110,110,110)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)


#Create blocks 
#I wanted to keep it as close to the original game as possible 
BLOCK1 = ['O','O','A','A','E','E']
BLOCK2 = ['O','U','U','A','E','I']
BLOCK3 = ['T','J','C','D','C','B']
BLOCK4 = ['N','K','Z','S','X','B']
BLOCK5 = ['M','Y','B','L','M','L']
BLOCK6 = ['T','C','C','T','M','S']
BLOCK7 = ['P','G','P','V','F','K']
BLOCK8 = ['N','Y','N','I','O','I']
BLOCK9 = ['N','N','H','H','R','R']
BLOCK10 = ['L','R','W','D','L','F']
BLOCK11 = ['L','R','R','D','G','G']
BLOCK12= ['W','P','T','H','H','T']

#Used to hold the "block" letters 
LETTER_LIST =  []


BLOCK_LIST=[BLOCK1,BLOCK2,BLOCK3,BLOCK4,BLOCK5,BLOCK6,
    BLOCK7,BLOCK8,BLOCK9,BLOCK10,BLOCK11,BLOCK12]



pygame.init()



def genBlocks():
        for block in BLOCK_LIST:
            LETTER_LIST.append(random.choice(block))
            

genBlocks()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Q-LESS")





LETTER1= pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[0]))),(50,50))

LETTER2= pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[1]))),(50,50))

LETTER3 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[2]))),(50,50))

LETTER4 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[3]))),(50,50))

LETTER5 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[4]))),(50,50))

LETTER6 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[5]))),(50,50))

LETTER7 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[6]))),(50,50))

LETTER8 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[7]))),(50,50))

LETTER9 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[8]))),(50,50))

LETTER10 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[9]))),(50,50))

LETTER11 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[10]))),(50,50))

LETTER12 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[11]))),(50,50))


class DragOperator:
    def __init__(self,rect) :
        self.rect = rect
        self.dragging = False
        self.rel_pos = (0,0)
        
    def collisioncheck(self):
        check_group = pygame.sprite.Group([letter for letter in group if letter != self.rect])
        if pygame.sprite.spritecollide(self, check_group, False):
#            pygame.draw.rect(self, GREEN, self.rect,6)
            print("test")
      



    def movementupdate(self, event_list):
        DragOperator.collisioncheck(self)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = self.rect.collidepoint(event.pos)
                self.rel_pos = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y
                
                
            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            if event.type == pygame.MOUSEMOTION and self.dragging:
                self.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]

 


class SpriteObject(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        super().__init__() 
        

        self.original_image = img
        pygame.draw.rect(self.original_image, BLUE, self.original_image.get_rect(),3)
        self.drag_image = pygame.Surface((300, 300), pygame.SRCALPHA)
        self.image = self.original_image 
        self.rect = self.original_image.get_rect(center = (x, y))

        self.drag = DragOperator(self.rect)
    
       
    def update(self, event_list):
        self.drag.movementupdate(event_list) 
        #self.image = self.image if self.drag.dragging else self.original_image



       

group = pygame.sprite.Group([

    SpriteObject(80, 500, LETTER1),
    SpriteObject(140,500, LETTER2),
    SpriteObject(200,500, LETTER3),
    SpriteObject(260,500, LETTER4),
    SpriteObject(320,500, LETTER5),
    SpriteObject(380,500, LETTER6),
    SpriteObject(440,500, LETTER7),
    SpriteObject(500,500, LETTER8),
    SpriteObject(560,500, LETTER9),
    SpriteObject(620,500, LETTER10),
    SpriteObject(680,500, LETTER11),
    SpriteObject(740,500, LETTER12)
])


TEST_DICT = {}

for key, value in zip(group,LETTER_LIST):
    TEST_DICT[key] = value


print(TEST_DICT)

def main():
    running = True
    moving = False
    FPS = 60
    GAMEFONT = pygame.font.SysFont('comicsans',25)
    print(LETTER_LIST)
    
    clock = pygame.time.Clock()
    
    
    def redraw_window():
        SCREEN.fill(WHITE)
        #L1.draw(SCREEN)
        SCREEN.blit(IMG1,LETTER1)
        pygame.draw.rect(SCREEN, GRAY,LETTER1,3)

        SCREEN.blit(IMG2,LETTER2)
        pygame.draw.rect(SCREEN, GRAY,LETTER2,3)

        #L2.draw(SCREEN)
        #Draw Text 
        heading_surface = GAMEFONT.render("Letters",1,(0,0,0))
        letter_surface = GAMEFONT.render(', '.join(LETTER_LIST),1,(0,0,0))
        SCREEN.blit(heading_surface,(300,50))
        #SCREEN.blit(letter_surface,(170,90))
       
        pygame.display.update()
    
    while running:
        
        clock.tick(FPS)
        #redraw_window()
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
        group.update(event_list)

        SCREEN.fill(GRAY)
        group.draw(SCREEN)
        pygame.display.flip()

                

main()

