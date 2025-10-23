import arcade
from entities.entity import Entity
from random import randint
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Dot(Entity):
    def __init__(self, window, name):
        super().__init__()
        self.name = name

        self.sprite.texture = arcade.make_circle_texture(32, arcade.color.WHITE)
        self.sprite.visible = False
        self.sprite.collidable = False
        self.sprite.position = (window.width/2, window.height/2)
        self.sprite.scale = 64 / self.sprite.width
        self.last = 0
        self.sprite.scale = 32 / self.sprite.width

    def spawn(self, window):
        if self.sprite.visible:
            return False
        elif not self.last >= 60:
            self.last+= 1
            return False
        
        self.sprite.position = (
            randint(20, window.width - 20),
            randint(20, window.height - 20)
        )
        self.last = 0

        self.sprite.visible = True
    
    def despawn(self):
        self.sprite.visible = False