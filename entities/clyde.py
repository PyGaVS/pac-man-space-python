import arcade
from entities.phantom import Phantom
from random import randrange

class Clyde(Phantom):
    def __init__(self, window):
        super().__init__()
        self.name = "clyde"

        self.sprite.texture = arcade.load_texture(f"assets/{self.name}/default/right/frame_1.gif")
        self.setAnimation()
        self.sprite.position = (window.width - 140, window.height - 220)
        self.sprite.scale = 64 / self.sprite.width


    def move(self, player, frame):
        if(frame % 30 == 0):
            self.chase(player)
        
        self.checkBorder()
        self.forward()
    
    def chase(self, player):
        random = randrange(5)
        if(random == 0):
            self.setDirection("U")
        elif(random == 1):
            self.setDirection("D")
        elif(random == 2):
            self.setDirection("R")
        elif(random == 3):
            self.setDirection("L")
        else:
            self.aim(720, 360)
        
        if self.isCloseTo({"x": player.sprite.center_x, "y": player.sprite.center_y}, 100):
            self.aim(player.sprite.center_x, player.sprite.center_y)