import arcade
from entities.phantom import Phantom

class Blinky(Phantom):
    def __init__(self, window):
        super().__init__()
        self.name = "blinky"

        self.sprite.texture = arcade.load_texture(f"assets/{self.name}/default/right/frame_1.gif")
        self.setAnimation()
        self.sprite.position = (window.width - 140, window.height - 70)
        self.sprite.scale = 64 / self.sprite.width

    def move(self, player, frame):
        if(frame % 15 == 0):
            self.chase(player)
        
        self.checkBorder()
        self.forward()
    
    def chase(self, player):
        self.aim(player.sprite.center_x, player.sprite.center_y)