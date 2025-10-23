import arcade
from utils.animation import Animation
from entities.entity import Entity
import utils.game_globals
from utils.input import Input

class Player(Entity):

    def __init__(self, window):
        super().__init__()

        self.sprite.texture = arcade.load_texture("assets/pac-man/default/frame_2.gif")
        
 
        self.sprite.position = (window.width/10, window.height/10)
        self.sprite.scale = 64 / self.sprite.width
        self.speed = 6
        self.name = "player"
        self.score = 0
        self.input = Input()

        self.speedBoost = 0
        self.diagonal = ""

        self.animation = Animation(
            [
                arcade.load_texture("assets/pac-man/default/frame_2.gif"),
                arcade.load_texture("assets/pac-man/default/frame_0.gif"),
                arcade.load_texture("assets/pac-man/default/frame_1.gif")
            ]
        )
    
    def on_key_press(self, key):
        input = self.getInput(key)

        self.setDirection(input)
        special = self.input.addInput(input)

        self.applySpecial(special)


    def setDirection(self, d):
        directions = {
            "R": 0,
            "L": 180,
            "U": -90,
            "D": 90,
            "RU": -45,
            "LU": -135,
            "LD": 135,
            "RD": 45
        }

        if directions.get(d, -1) != -1: self.direction = d
        self.sprite.angle = directions.get(d, 0)
        self.speedBoost = 0

    def move(self):
        self.checkBorder()
        self.forward(self.speedBoost)
    
    def getInput(self, key):
        input = ""
        if key == arcade.key.RIGHT:
            input = "R"
        elif key == arcade.key.LEFT:
            input = "L"
        elif key == arcade.key.UP:
            input = "U"
        elif key == arcade.key.DOWN:
            input = "D"
        
        return input
    
    def applySpecial(self, special):
        if special == "speed":
            self.speedBoost = self.speed/2 + 1
        if special in("RU", "LU", "LD", "RD"):
            self.setDirection(special)