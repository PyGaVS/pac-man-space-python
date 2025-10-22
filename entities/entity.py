import arcade
from utils.animation import Animation

class Entity():
    def __init__(self):
        self.direction = "R"
        self.sprite = arcade.Sprite()
        self.speed = 5
        self.animation = Animation([])

    
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