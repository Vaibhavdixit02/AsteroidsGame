bif = "bg.jpg"
mif = "bg - Copy.jpg"
nif = "bg - Copy - Copy.jpg"
sif = "table.jpg"
q = "1.jpg"
w = "2.jpg"
e = "3.jpg"
r = "4.jpg"
t = "5.jpg"
y = "6.jpg"
u = "7.jpg"
i = "8.jpg"
p = "9.jpg"
a = "10.jpg"
s = "11.jpg"
d = "missile.jpg"
f = "asteroids1.jpg"
g = "asteroids2.jpg"

import pygame, sys, random, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,600),0,32)
pygame.font.init()
selected = [(100000,100000)]
ships = [1]
background1 = pygame.image.load(bif).convert_alpha()
background2 = pygame.image.load(mif).convert_alpha()
background3 = pygame.image.load(nif).convert_alpha()
choice = pygame.image.load(sif).convert_alpha()
ship1 = pygame.image.load(q).convert_alpha()
ship2 = pygame.image.load(w).convert_alpha()
ship3 = pygame.image.load(e).convert_alpha()
ship4 = pygame.image.load(r).convert_alpha()
ship5 = pygame.image.load(t).convert_alpha()
ship6 = pygame.image.load(y).convert_alpha()
ship7 = pygame.image.load(u).convert_alpha()
ship8 = pygame.image.load(i).convert_alpha()
ship9 = pygame.image.load(p).convert_alpha()
ship10 = pygame.image.load(a).convert_alpha()
ship11 = pygame.image.load(s).convert_alpha()
missile1 = pygame.image.load(d).convert_alpha()
asteroid1 = pygame.image.load(f).convert_alpha()
asteroid2 = pygame.image.load(g).convert_alpha()
class buttonsmall():


    def __init__(self,x,y,screen,mouse):


        self.create(screen,x,y)
        self.isclicked(x,y,mouse)
    def create(self,screen,x,y):
        pygame.draw.rect(screen,(100,100,0),(x,y,20,20))


    def isclicked(self,x,y,mouse):
        if event.type == MOUSEBUTTONDOWN:
            if x < mouse[0] < x+20 and y < mouse[1] <y+20 :
                pygame.draw.lines(screen,(100,50,0),1,((x,y),(x+20,y),(x+20,y+20),(x,y+20)),5)
                selected.pop()
                selected.append((x,y))

                if selected[0][1]== 345:
                    if selected[0][0] == 250:
                        ships.pop()
                        ships.append(1)

                    elif selected[0][0] ==330:
                        ships.pop()
                        ships.append(2)
                    elif selected[0][0] ==410:
                        ships.pop()
                        ships.append(3)
                    elif selected[0][0] ==490:
                        ships.pop()
                        ships.append(4)
                    elif selected[0][0] ==550:
                        ships.pop()
                        ships.append(5)
                    elif selected[0][0] ==620:
                        ships.pop()
                        ships.append(6)
                elif selected[0][1] ==450:
                    if selected[0][0] ==250:
                        ships.pop()
                        ships.append(7)
                    elif selected[0][0] ==350:
                        ships.pop()
                        ships.append(8)
                    elif selected[0][0] ==450:
                        ships.pop()
                        ships.append(9)
                    elif selected[0][0] ==530:
                        ships.pop()
                        ships.append(10)
                    elif selected[0][0] ==620:
                        ships.pop()
                        ships.append(11)





        if event.type == MOUSEMOTION:
            if x < mouse[0] < x + 20 and y < mouse[1] < y + 20:
                pygame.draw.rect(screen, (100, 50, 0), (x, y, 20, 20))

        else:
            return False
shipx = 10
shipy = 300
class spaceship(pygame.sprite.Sprite):
    def __init__(self,screen1,speed,t):
        super(spaceship, self).__init__()
        self.create(screen1,t,shipx,shipy)
        self.speed = speed
        if t == 1:
            self.image = ship1
            self.rect = self.image.get_rect()
        elif t == 2:
            self.image = ship2
            self.rect = self.image.get_rect()
        elif t == 3:
            self.image = ship3
            self.rect = self.image.get_rect()
        elif t == 4:
            self.image = ship4
            self.rect = self.image.get_rect()
        elif t == 5:
            self.image = ship5
            self.rect = self.image.get_rect()
        elif t == 6:
            self.image = ship6
            self.rect = self.image.get_rect()
        elif t == 7:
            self.image = ship7
            self.rect = self.image.get_rect()
        elif t == 8:
            self.image = ship8
            self.rect = self.image.get_rect()
        elif t == 9:
            self.image = ship9
            self.rect = self.image.get_rect()
        elif t == 10:
            self.image = ship10
            self.rect = self.image.get_rect()
        elif t == 11:
            self.image = ship11
            self.rect = self.image.get_rect()
    def create(self,screen1,t,shipx,shipy):

        if t == 1:
            screen1.blit(ship1,(shipx,shipy))
        elif t==2:
            screen1.blit(ship2, (shipx, shipy))
        elif t==3:
            screen1.blit(ship3, (shipx, shipy))
        elif t==4:
            screen1.blit(ship4, (shipx, shipy))
        elif t==5:
            screen1.blit(ship5, (shipx, shipy))
        elif t==6:
            screen1.blit(ship6, (shipx, shipy))
        elif t==7:
            screen1.blit(ship7, (shipx,shipy))
        elif t==8:
            screen1.blit(ship8, (shipx,shipy))
        elif t==9:
            screen1.blit(ship9, (shipx,shipy))
        elif t==10:
            screen1.blit(ship10, (shipx,shipy))
        elif t==11:
            screen1.blit(ship11, (shipx,shipy))


colour = (100,0,0)
class missile(pygame.sprite.Sprite):
    def __init__(self,u,v,screen2):
        super(missile, self).__init__()
        self.create(screen2,u,v)
        self.move(screen2,u,v)
    def create(self,screen2,x, y):
        screen2.blit(missile1, (x,y))
    def move(self,screen2,x, y):
        x = x + 10
        self.create(screen2,x,y)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, surface, u, v):
        super(Projectile, self).__init__()
        self.image = missile1
        self.x = u
        self.y = v
        self.renderer = surface
        self.speed = 10
        self.rect = self.image.get_rect()

    def move(self, time):
        self.x += time*self.speed
        self.renderer.blit(missile1, (self.x, self.y))

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,screen3):
        super(Asteroid, self).__init__()
        self.image = asteroid1
        self.x = random.randint(0,1000)
        self.y = random.randint(0,600)
        self.renderer = screen3
        self.rect = self.image.get_rect()


    def draw(self):
        self.renderer.blit(asteroid1, (self.x, self.y))
        self.x += random.randint(0,5)
        self.y += random.randint(0,5)
        self.x = self.x % 1000
        self.y = self.y % 600









level = 3
score = 0
scorelist = [0]
angle = 0
asteroids = pygame.sprite.Group()
pygame.mixer.music.load('music.mp3')
missiles = pygame.sprite.Group()
m = Projectile(screen,100,700)
missiles.add(m)
q = 0
o =1
color1 = (30,70,100)
listp = []
missileLaunched = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:

            pygame.quit()
            sys.exit()
    for i in range(0,1000,300):
        for j in range(0,600,300):
            screen.blit(background1, (i, j))
    for i in range(200,1000,300):
        for j in range(200,600,300):
            screen.blit(background2, (i, j))
    for i in range(200,1000,300):
        for j in range(200,600,300):
            screen.blit(background3, (i, j))

    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font,50)
    font_renderer1 = pygame.font.Font(default_font,70)
    label = font_renderer.render("Start",1,(100,0,100) )
    label2 = font_renderer1.render("Choose a Ship",1,(200,0,100))
    font_renderer2 = pygame.font.Font(default_font, 20)
    label3 = font_renderer2.render("SCORE",1,(150,0,0))
    label4 = font_renderer2.render(str(score),1,(150,0,0))
    label5 = font_renderer.render("High Score",1,(120,20,30))
    label6 = font_renderer.render("Last Score", 1, (120, 50, 30))
    label7 = font_renderer.render(str(scorelist[len(scorelist)-1]),1,(120,50,30))
    label8 = font_renderer.render(str(max(scorelist)), 1, (120, 20, 30))
    mouse = pygame.mouse.get_pos()

    if event.type == MOUSEBUTTONDOWN and 375 < mouse[0] <575 and 250< mouse[1] <325:
        o = 0


    if o == 1:
        score = 0
        shipx = random.randint(0,1000)
        shipy = random.randint(0,600)
        screen.blit(label6,(150,20))
        screen.blit(label7,(430,20))
        screen.blit(label5,(150,65))
        screen.blit(label8,(430,65))
        pygame.draw.rect(screen, (100, 10, 0), (375, 250, 200, 75))
        pygame.mixer.music.play(-1)
        screen.blit(label,(420,265))
        screen.blit(choice,(250,340))
        screen.blit(label2,(260,165))
        for i in range(250,550,80):
            bt = buttonsmall(i,345,screen,mouse)
        bt = buttonsmall(550,345,screen,mouse)
        bt = buttonsmall(620,345,screen,mouse)
        for i in range(250, 550, 100):
            bt = buttonsmall(i,450,screen,mouse)
        bt = buttonsmall(530, 450, screen, mouse)
        bt = buttonsmall(620, 450, screen, mouse)
        for i in selected:
            pygame.draw.lines(screen, (100, 50, 0), 1, ((selected[0][0], selected[0][1]), (selected[0][0] + 20, selected[0][1]), (selected[0][0] + 20, selected[0][1] + 20), (selected[0][0], selected[0][1] + 20)), 5)

    elif o == 0:
        pygame.init()
        ship = spaceship(screen,10,ships[0])
        clock = pygame.time.Clock()
        asteroid13 = Asteroid(screen)

        if asteroids.__len__() < level and asteroids.__len__() > 0:
            for asts in asteroids:
                if abs(asts.x - asteroid13.x ) > 74 and abs(asts.y - asteroid13.y ) > 59:

                    asteroids.add(asteroid13)
        elif asteroids.__len__() == 0:
            asteroids.add(asteroid13)
        screen.blit(label3,(10,10) )
        screen.blit(label4,(90,10))
        for ast in asteroids:
            ast.draw()
        times = pygame.time.get_ticks()
        if times % 5000 == 0:
            level += 1
            print times









    keys = pygame.key.get_pressed()
    if event.type == KEYDOWN:
        if event.key == K_SPACE and not missileLaunched and o == 0:
            miss = Projectile(screen,shipx,shipy)
            missiles.add(miss)
            missileLaunched = True
    elif event.type == KEYUP:
        if event.key == K_SPACE and missileLaunched:
            missileLaunched = False




    for misses in missiles:
        misses.move(2)
        if misses.x > 1000:
            missiles.remove(misses)



    angle = 0
    if keys[K_UP]:
        shipy -= 5
        shipy = abs(shipy)
        shipy = shipy %600

    if keys[K_DOWN]:
        shipy += 5
        shipy = shipy % 600

    if keys[K_RIGHT]:
        shipx += 5
        shipx = shipx % 1000

    if keys[K_LEFT]:
        shipx -= 5
        shipx = shipx % 1000



    if event.type == pygame.KEYUP:
        decc = 0.05
        if event.key == K_RIGHT:
            while decc > 0:
                shipx += decc
                decc = decc - 0.01
        if event.key == K_DOWN:
            while decc > 0:
                shipy += decc
                decc = decc - 0.01
        if event.key == K_UP:
            while decc > 0:
                shipy -= decc
                decc = decc - 0.01
        if event.key == K_LEFT:
            while decc > 0:
                shipx == decc
                decc = decc - 0.01

    for asts in asteroids:
        for mis in missiles:
            if abs(asts.x - mis.x + 16) < 58 and abs(asts.y - mis.y +12) < 48:
                asteroids.remove(asts)
                missiles.remove(mis)
                score += 1
                scorelist.append(score)


    for asts in asteroids:
        if abs(shipx-asts.x) < ship.rect.width/2 + 37 and abs(shipy-asts.y) < ship.rect.height/2 + 30:
            o = 1








    pygame.display.update()
