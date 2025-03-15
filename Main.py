#importantationatitationinitatimportatnte
import pygame as p


_display = p.display
class CPU():
    window = None
    Screen_width = 800
    Screen_height = 500
    def __init__(self) -> None:
        pass
    def begin(self):
        _display.init()
        CPU.window = p.display.set_mode([CPU.Screen_width, CPU.Screen_height])
        _display.set_caption('Tank Wars')
        while True: 
            CPU.window.fill(p.Color(150, 150, 255))
            self.get_event()
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
    def end(self):
        print('Thank you for playing. You have unofficially died of getting hit by a bullet shot by the enemy during the fight.')
        exit()

class tank():
    def __init__(self) -> None:
        pass
    def move(self):
        pass
    def shoot(self):
        pass
    def display(self):
        pass


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
