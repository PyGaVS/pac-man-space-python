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
            self.direction = "R"
            self.sprite.angle = 0
        elif key == arcade.key.LEFT:
            self.direction = "L"
            self.sprite.angle = 180
        elif key == arcade.key.UP:
            self.direction = "U"
            self.sprite.angle = -90
        elif key == arcade.key.DOWN:
            self.direction = "D"
            self.sprite.angle = 90