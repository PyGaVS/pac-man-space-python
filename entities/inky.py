import arcade
from utils.animation import Animation
from entities.phantom import Phantom

class Inky(Phantom):
    def __init__(self, window):
        super().__init__()
        self.name = "inky"

        self.sprite.texture = arcade.load_texture(f"assets/{self.name}/default/right/frame_1.gif")
        self.setAnimation()
        self.sprite.position = (window.width - 140, window.height - 220)
        self.sprite.scale = 64 / self.sprite.width

    def move(self, player, frame, phantoms):
        if(frame % 30 == 0):
            self.chase(player, phantoms)
        
        self.checkBorder()
        self.forward()
    
    def chase(self, player, phantoms: Phantom):
        for phantom in phantoms:
            if(self.isCloseTo({"x": phantom.sprite.center_x, "y": phantom.sprite.center_y}) and phantom.name != "inky"):
                self.aimAway(phantom.sprite.center_x, phantom.sprite.center_y)
                return
        
        self.aim(player.sprite.center_x, player.sprite.center_y)