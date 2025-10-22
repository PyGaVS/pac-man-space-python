import arcade
from utils.animation import Animation
from entities.entity import Entity

class Phantom(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 3
        self.name = "blinky"
        self.direction = "L"
    
    def setDirection(self, direction):
        self.direction = direction

    def aim(self, x, y):
        dx = x - self.sprite.center_x
        dy = y - self.sprite.center_y

        if abs(dx) >= abs(dy):
            if dx < 0:
                self.setDirection("L")
            else:
                self.setDirection("R")
        else:
            if dy < 0:
                self.setDirection("D")
            elif dy > 0:
                self.setDirection("U")
    
    def setAnimation(self):
        self.animation = Animation(
            [
                arcade.load_texture(f"assets/{self.name}/default/right/frame_0.gif"),
                arcade.load_texture(f"assets/{self.name}/default/right/frame_1.gif")
            ]
        )
        