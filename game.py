import sys
import random as rd
import pygame
from pygame.locals import *
from classes import *
from DB import *
class Game:

    def play(self):
        pygame.init()
        db = DB() 

        db.clear_base()
        db.insert_2elements("bar_info", 100, 20)

        fps = 60
        fpsClock = pygame.time.Clock()
        j = 0
        list1 = []

        width, height = 640, 480
        screen = pygame.display.set_mode((width, height))

        c123 = (255, 100, 00)

        ship = Ship(c123, screen, db.fetch_one("bar_info","width"),db.fetch_one("bar_info","height"),100,height-20) 

        font = pygame.font.Font('freesansbold.ttf', 32)
 
        text = font.render('color', True, (255, 255, 255), (0, 0, 0))
 
        textRect = text.get_rect()
 
        textRect.center = (width * 0.9, height * 0.1)



        index = 0
        index1 = index-1



        while True:
          c1 = rn.randint(0,255)
          c2 = rn.randint(0,255)
          c3 = rn.randint(0,255)
          color = (c1,c2,c3)
          x = UFO(color, screen, 20,20,rd.randint(0,width),0) 
  
          screen.fill((0, 0, 0))
          screen.blit(text, textRect)
          ticks=pygame.time.get_ticks()
          for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()
  
          j+=1
          if(j>100):
             list1.append(x)
             j=0
          for i in list1:
             i.draw_it(screen)
             i.move_it(ticks/5000)


          ship.controll_it()
          ship.draw_it(screen)

          for i in list1:
            if(ship.collide(i)==1):
               db.update_value("bar_info","width",1)

               ship.expand(db.fetch_one("bar_info","width"))
               ship.change_color(i.return_color())
      

               index+=1
               index1+=1

               db.add_3elements("colors",i.return_color(),index)
               if index == 1:
                  text = font.render('color', True,(255,255,255), (db.fetch_color(index)))
               if index>= 2:
                 text = font.render('color', True, (db.fetch_color(index)), (db.fetch_color(index1)))
                 list1.remove(i)

          pygame.display.flip()
          pygame.display.update()
          fpsClock.tick(fps)