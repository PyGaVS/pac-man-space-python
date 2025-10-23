import arcade
from utils.animation import Animation
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Entity():
    def __init__(self):
        self.direction = "R"
        self.sprite = arcade.Sprite()
        self.speed = 5
        self.animation = Animation([])
        self.name=""

    
    def forward(self):
        moves = {
            "R": (self.speed, 0),
            "L": (-self.speed, 0),
            "U": (0, self.speed),
            "D": (0, -self.speed)
        }

        dx, dy = moves.get(self.direction, (0, 0))
        self.sprite.center_x += dx
        self.sprite.center_y += dy

    def animate(self, dt):
        newFrame = self.animation.update(dt)
        if newFrame:
            self.sprite.texture = newFrame

    def checkBorder(self):
        if self.sprite.center_x + self.sprite.width/2 >= SCREEN_WIDTH:
            self.setDirection("L")
        elif self.sprite.center_x - self.sprite.width/2 <= 1:
            self.setDirection("R")
        elif self.sprite.center_y + self.sprite.height/2 >= SCREEN_HEIGHT:
            self.setDirection("D")
        elif self.sprite.center_y - self.sprite.height/2 <= 1:
            self.setDirection("U")

    def setDirection():
        pass

    def isCloseTo(self, pos, range = 1500):
        return abs(self.sprite.center_x - pos["x"]) < range and abs(self.sprite.center_y - pos["y"]) < range