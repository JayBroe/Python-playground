import pygame as pg






class Object():
    x = pg
    def __init__(self, color, screen, width, height, pos_x, pos_y):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def move_it(self):
        pass
    def draw_it(self):
        pass
    def controll_it(self):
        pass
    def collision(self):
        pass
    def change_color(self):
        pass
    def return_color(self):
        pass


class UFO(Object): 
    def __init__(self,color, screen, width, height, pos_x, pos_y ):
        super().__init__(color, screen, width, height, pos_x, pos_y)
        
    def move_it(self, dt):
        self.pos_y += dt
    def collision(self):
        if self.pos_y>640:
            return 1
    def return_color(self):
        return self.color


    def draw_it(self, screen):
        self.x.draw.rect(screen, (self.color[0], self.color[1], self.color[2]), 
                         pg.Rect(self.pos_x,self.pos_y,
                                 self.width,self.height))   

    def collide(self, UFO):
        leftA = UFO.pos_x
        rightA = UFO.pos_x + UFO.width
        topA = UFO.pos_y
        bottomA = UFO.pos_y + UFO.height;  

        leftB = self.pos_x
        rightB = self.pos_x + self.width
        topB = self.pos_y
        bottomB = self.pos_y + self.height

        if (bottomA <= topB):
            return 0
        if (topA >= bottomB):
            return 0

        if(rightA <= leftB):
            return 0

        if(leftA >= rightB):
            return 0
        else:
            return 1


class Ship(Object):
    def __init__(self,color, screen, width, height, pos_x, pos_y ):
        super().__init__(color, screen, width, height, pos_x, pos_y)

    def draw_it(self, screen):
        self.x.draw.rect(screen, (self.color[0], self.color[1], self.color[2]), 
                         pg.Rect(self.pos_x,self.pos_y,
                                 self.width,self.height))    

    def collide(self, UFO):
        leftA = UFO.pos_x
        rightA = UFO.pos_x + UFO.width
        topA = UFO.pos_y
        bottomA = UFO.pos_y + UFO.height;  

        leftB = self.pos_x
        rightB = self.pos_x + self.width
        topB = self.pos_y
        bottomB = self.pos_y + self.height

        if (bottomA <= topB):
            return 0
        if (topA >= bottomB):
            return 0

        if(rightA <= leftB):
            return 0

        if(leftA >= rightB):
            return 0
        else:
            return 1
        
    def return_color(self):
        return self.color 

    def change_color(self,color):
        self.color = color


    def controll_it(self):
        keys = pg.key.get_pressed()
        if keys[pg.key.key_code("A")]:
            self.pos_x+=-7    
        if keys[pg.key.key_code("D")]:
            self.pos_x+=7      

    def expand(self, ine):
        self.width+=ine        