import os
import pygame as pg
from pygame.locals import *
import random
import urllib.request
from bs4 import BeautifulSoup

pg.font.init()


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



pg.init()





SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("QLess-Test")



def gen_blocks():
        for block in BLOCK_LIST:
            LETTER_LIST.append(random.choice(block))
            

gen_blocks()


bg = pg.image.load(os.path.join('images','background.jpg'))

LETTER1 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[0]))),(50,50))

LETTER2= pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[1]))),(50,50))

LETTER3 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[2]))),(50,50))

LETTER4 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[3]))),(50,50))

LETTER5 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[4]))),(50,50))

LETTER6 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[5]))),(50,50))

LETTER7 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[6]))),(50,50))

LETTER8 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[7]))),(50,50))

LETTER9 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[8]))),(50,50))

LETTER10 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[9]))),(50,50))

LETTER11 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[10]))),(50,50))

LETTER12 = pg.transform.scale(pg.image.load(os.path.join('images','{}.png'.format(LETTER_LIST[11]))),(50,50))



        


class SpriteObject(pg.sprite.Sprite):
    def __init__(self,x,y,img,name):
        #self.x = x
        #self.y = y
        self.name = name
        super().__init__() 
        self.original_image = img
        self.test = pg.draw.rect(self.original_image, BLUE, self.original_image.get_rect(),3)
        self.drag_image = pg.Surface((300, 300), pg.SRCALPHA)
        self.image = self.original_image 
        self.rect = self.original_image.get_rect(center = (x, y))
        self.drag = Gameplay(self.rect)


    def wall_collision_check(self):
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        elif self.rect.left <=0:
            self.rect.left = 0

        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        elif self.rect.top <=0:
            self.rect.top = 0



    def collision_check(self):
        collision_tolerance = 10

        check_group = pg.sprite.Group([letter for letter in group if letter != self.rect])
        if pg.sprite.spritecollideany(self, check_group):
            self.test = pg.draw.rect(self.original_image, RED, self.original_image.get_rect(),3)
            for i in check_group:
                if self.rect.colliderect(i):
                    if abs(self.rect.right - i.rect.left) <= collision_tolerance:
                        self.rect.right = i.rect.left
                    
                        #self.rect.midright = i.rect.midleft
                        #self.rect.bottomright = i.rect.bottomleft

                    elif abs(self.rect.left - i.rect.right) <= collision_tolerance:
                        self.rect.left = i.rect.right
            
                        #self.rect.midleft = i.rect.midright
                        #self.rect.bottomleft = i.rect.bottomright
                    
                    elif abs(self.rect.top - i.rect.bottom) <= collision_tolerance:
                        self.rect.top = i.rect.bottom
                        #self.rect.midtop = i.rect.midbottom
                        #self.rect.topleft = i.rect.bottomleft
                    
                    elif abs(self.rect.bottom - i.rect.top) <= collision_tolerance:
                        self.rect.bottom = i.rect.top
                        #self.rect.midbottom = i.rect.midtop
                        #self.rect.bottomleft = i.rect.topleft
                        
              
        else:
            self.test = pg.draw.rect(self.original_image, BLUE, self.original_image.get_rect(),3)        
            #self.test = pg.draw.rect(self.original_image, GRAY, self.original_image.get_rect(),3)
        #print(test)



    
    def word_checker(self):
        for i in group:
            if self != i and self.rect.colliderect(i.rect):
                print(i.name)




    def update(self, event_list):
        SpriteObject.wall_collision_check(self)
        SpriteObject.collision_check(self)
        self.drag.movement_update(event_list) 
        SpriteObject.word_checker(self)
        Gameplay.check_word()
        
        
    

        
  

            



class Gameplay:
    def __init__(self,rect) :
        self.rect = rect
        self.dragging = False
        self.rel_pos = (0,0)
                       
    def movement_update(self, event_list):
        for event in event_list:
            
            if event.type == pg.MOUSEBUTTONDOWN:
                self.dragging = self.rect.collidepoint(event.pos)
                self.rel_pos = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y

            elif event.type == pg.MOUSEMOTION and self.dragging:
                self.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]
            
                
            elif event.type == pg.MOUSEBUTTONUP:
                self.dragging = False
            
    def reset_game():
        pass

    def win_condition_check():
        pass

    def check_word():
        pass


group = pg.sprite.Group([

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
    
    clock = pg.time.Clock()
    
    while running:
        
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                running = False
        group.update(event_list)

        SCREEN.fill(GRAY)
        SCREEN.blit(bg,(0,0))
        group.draw(SCREEN)
        pg.display.flip()

                

main()

