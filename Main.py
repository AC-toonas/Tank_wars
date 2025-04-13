#importantationatitationinitatimportatnte
import pygame as p


_display = p.display
class CPU():
    window = None
    Screen_width = 800
    Screen_height = 500
    Tank_player = None
    def __init__(self) -> None:
        pass
    def begin(self):
        _display.init()
        CPU.window = p.display.set_mode([CPU.Screen_width, CPU.Screen_height])
        CPU.Tank_player = tank(300, 150)
        _display.set_caption('Tank Wars')
        while True: 
            CPU.window.fill(p.Color(150, 150, 255))
            self.get_event()
            CPU.window.blit(self.get_text('Remaining %d tanks'%5), (5, 5))
            CPU.Tank_player.display()
            _display.update()

    def get_event(self):
        el = p.event.get()
        for event in el:
            if event.type == p.QUIT:
                self.end()
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    pass
                if event.key == p.K_RIGHT:
                    pass
                if event.key == p.K_UP:
                    pass
                if event.key == p.K_DOWN:
                    pass
                if event.key == p.K_SPACE:
                    pass
    def get_text(self, text):
        p.font.init()
        f = p.font.SysFont('kaiti',18)
        txtcanvs = f.render(text, True, p.Color(250, 250, 255))
        return txtcanvs
    def end(self):
        print('Thank you for playing. You have unofficially died of getting hit by a bullet shot by the enemy during the fight.')
        exit()

class tank():
    def __init__(self, left, top):
        self.images = {'U':p.image.load('c:/Users/14168/OneDrive/Desktop/Mingxi_Chen/Python/GUI interface/pygame/Tank_wars/Player_Tank_up.png'), 'D':p.image.load('c:/Users/14168/OneDrive/Desktop/Mingxi_Chen/Python/GUI interface/pygame/Tank_wars/Player_Tank_down.png'), 'L':p.image.load('c:/Users/14168/OneDrive/Desktop/Mingxi_Chen/Python/GUI interface/pygame/Tank_wars/Player_Tank_left.png'), 'R':p.image.load('c:/Users/14168/OneDrive/Desktop/Mingxi_Chen/Python/GUI interface/pygame/Tank_wars/Player_Tank_right.png')}
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
    def move(self):
        pass
    def shoot(self):
        pass
    def display(self):
        self.image = self.images[self.direction]
        CPU.window.blit(self.image, self.rect)

class player(tank):
    def __init__(self) -> None:
        pass


class enemy(tank):
    def __init__(self) -> None:
        pass


class bullet():
    def __init__(self) -> None:
        pass
    def move(self):
        pass
    def display(self):
        pass


class Explode():
    def __init__(self) -> None:
        pass
    def explode(self):
        pass


class wall():
    def __init__(self) -> None:
        pass
    def showwall():
        pass


class music():
    def __init__(self) -> None:
        pass
    def play():
        pass
c = CPU()
c.begin()
