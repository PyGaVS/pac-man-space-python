import arcade
from utils.animation import Animation
from entities.entity import Entity
class Player(Entity):
    def __init__(self, window):
        super().__init__()

        self.sprite.texture = arcade.load_texture("assets/pac-man/default/frame_2.gif")
        
 
        self.sprite.position = (window.width/10, window.height/10)
        self.sprite.scale = 64 / self.sprite.width
        self.speed = 6

        self.animation = Animation(
            [
                arcade.load_texture("assets/pac-man/default/frame_2.gif"),
                arcade.load_texture("assets/pac-man/default/frame_0.gif"),
                arcade.load_texture("assets/pac-man/default/frame_1.gif")
            ]
        )
    
    def on_key_press(self, key):
        if key == arcade.key.RIGHT:
            self.setDirection("R")
        elif key == arcade.key.LEFT:
            self.setDirection("L")
        elif key == arcade.key.UP:
            self.setDirection("U")
        elif key == arcade.key.DOWN:
            self.setDirection("D")

    def setDirection(self, d):
        directions = {
            "R": 0,
            "L": 180,
            "U": -90,
            "D": 90
        }

        self.direction = d
        self.sprite.angle = directions.get(d, 0)

    def move(self):
        self.checkBorder()
        self.forward()