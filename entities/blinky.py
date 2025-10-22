import arcade
from utils.animation import Animation
from entities.phantom import Phantom

class Blinky(Phantom):
    def __init__(self, window):
        super().__init__()
        self.sprite.texture = arcade.load_texture("assets/blinky/default/right/frame_1.gif")
        
 
        self.sprite.position = (window.width - window.width/10, window.height - window.height/10)
        self.sprite.scale = 64 / self.sprite.width

    def move(self, player, frame):
        if(frame % 15 == 0):
            self.chase(player)

        self.forward()
    
    def chase(self, player):
        self.aim(player.sprite.center_x, player.sprite.center_y)