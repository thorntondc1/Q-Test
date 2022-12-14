import pygame
import os
from pygame.locals import *
import random
import urllib.request
from bs4 import BeautifulSoup

pygame.font.init()


WIDTH = 800
HEIGHT = 600

BLACK = (0,0,0)
GRAY = (110,110,110)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255,0,0)


#Create blocks 
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





SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QLess-Test")


def genBlocks():
        for block in BLOCK_LIST:
            LETTER_LIST.append(random.choice(block))
            

genBlocks()


LETTER1 = pygame.transform.scale(pygame.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[0]))),(50,50))

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



        


class SpriteObject(pygame.sprite.Sprite):
    def __init__(self,x,y,img,name):
        #self.x = x
        #self.y = y
        self.name = name
        super().__init__() 
        self.original_image = img
        self.test = pygame.draw.rect(self.original_image, BLUE, self.original_image.get_rect(),3)
        self.drag_image = pygame.Surface((300, 300), pygame.SRCALPHA)
        self.image = self.original_image 
        self.rect = self.original_image.get_rect(center = (x, y))
        self.drag = DragOperator(self.rect)


    def wall_collision_check(self):
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        elif self.rect.left <=0:
            self.rect.left = 0

        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        elif self.rect.top <=0:
            self.rect.top = 0



    def collisioncheck(self):
        collision_tolerance = 5


        check_group = pygame.sprite.Group([letter for letter in group if letter != self.rect])
        if pygame.sprite.spritecollideany(self, check_group):
            self.test = pygame.draw.rect(self.original_image, RED, self.original_image.get_rect(),3)
            for i in check_group:
                if self.rect.colliderect(i):
                    if abs(self.rect.right - i.rect.left) <= collision_tolerance:
                        self.rect.right = i.rect.left

                    elif abs(self.rect.left - i.rect.right) <= collision_tolerance:
                        self.rect.left = i.rect.right
                    
                    elif abs(self.rect.top - i.rect.bottom) <= collision_tolerance:
                        self.rect.top = i.rect.bottom
                    
                    elif abs(self.rect.bottom - i.rect.top) <= collision_tolerance:
                        self.rect.bottom = i.rect.top
                        
                            
                   

            




          

      

        else:
            self.test = pygame.draw.rect(self.original_image, BLUE, self.original_image.get_rect(),3)        
            #self.test = pygame.draw.rect(self.original_image, GRAY, self.original_image.get_rect(),3)
        #print(test)




    def update(self, event_list):
        SpriteObject.wall_collision_check(self)
        SpriteObject.collisioncheck(self)
        self.drag.movementupdate(event_list) 
        
        
        
        
  

            



class DragOperator:
    def __init__(self,rect) :
        self.rect = rect
        self.dragging = False
        self.rel_pos = (0,0)
                       
          

    def movementupdate(self, event_list):
        for event in event_list:
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = self.rect.collidepoint(event.pos)
                self.rel_pos = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y

            elif event.type == pygame.MOUSEMOTION and self.dragging:
                self.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]
            
                
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            


group = pygame.sprite.Group([

    SpriteObject(80, 500, LETTER1, LETTER_LIST[0]),
    SpriteObject(140,500, LETTER2, LETTER_LIST[1]),
    SpriteObject(200,500, LETTER3, LETTER_LIST[2]),
    SpriteObject(260,500, LETTER4, LETTER_LIST[3]),
    SpriteObject(320,500, LETTER5, LETTER_LIST[4]),
    SpriteObject(380,500, LETTER6, LETTER_LIST[5]),
    SpriteObject(440,500, LETTER7,LETTER_LIST[6]),
    SpriteObject(500,500, LETTER8, LETTER_LIST[7]),
    SpriteObject(560,500, LETTER9, LETTER_LIST[8]),
    SpriteObject(620,500, LETTER10, LETTER_LIST[9]),
    SpriteObject(680,500, LETTER11, LETTER_LIST[10]),
    SpriteObject(740,500, LETTER12, LETTER_LIST[11])
])

       



def main():
    running = True
    
    print(LETTER_LIST)
    
    clock = pygame.time.Clock()
    
    while running:
        
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
        group.update(event_list)

        SCREEN.fill(GRAY)
        group.draw(SCREEN)
        pygame.display.flip()

                

main()

