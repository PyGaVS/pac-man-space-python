import arcade
from utils.animation import Animation
from entities.entity import Entity

class Phantom(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.name = "blinky"
        self.direction = "L"
    
    def setDirection(self, direction):
        if direction == "L":
            self.animation = Animation(self.textures["left"])
        elif direction == "R":
            self.animation = Animation(self.textures["right"])
        elif direction == "D":
            self.animation = Animation(self.textures["down"])
        elif direction == "U":
            self.animation = Animation(self.textures["up"])

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
            else:
                self.setDirection("U")

    def aimAway(self, x, y):
        dx = x - self.sprite.center_x
        dy = y - self.sprite.center_y

        if abs(dx) <= abs(dy):
            if dx > 0:
                self.setDirection("L")
            else:
                self.setDirection("R")
        else:
            if dy > 0:
                self.setDirection("D")
            else:
                self.setDirection("U")
    
    def setAnimation(self):
        self.textures = {}
        for d in ["right", "up", "down", "left"]:
            if d == "left":
                self.textures[d] = [
                    arcade.load_texture(f"assets/{self.name}/default/right/frame_0.gif"),
                    arcade.load_texture(f"assets/{self.name}/default/right/frame_1.gif"),
                ]

                self.textures[d] = [texture.flip_horizontally() for texture in self.textures[d]]
            else:
                self.textures[d] = [
                    arcade.load_texture(f"assets/{self.name}/default/{d}/frame_0.gif"),
                    arcade.load_texture(f"assets/{self.name}/default/{d}/frame_1.gif"),
                ]

        self.animation = Animation(self.textures["left"])
        