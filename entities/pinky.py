import arcade
from utils.animation import Animation
from entities.phantom import Phantom

class Pinky(Phantom):
    def __init__(self, window):
        super().__init__()
        self.name = "pinky"

        self.sprite.texture = arcade.load_texture(f"assets/{self.name}/default/right/frame_1.gif")
        self.setAnimation()
        self.sprite.position = (window.width - 290, window.height - 220)
        self.sprite.scale = 64 / self.sprite.width


    def move(self, player, frame):
        if(frame % 30 == 0):
            self.chase(player)

        self.checkBorder()
        self.forward()
    
    def chase(self, player):
        targetX, targetY = player.sprite.center_x, player.sprite.center_y
        targetRange = self.getTargetRange(player.sprite.center_x, player.sprite.center_y, 600)


        moves = {
            "R": (targetX + targetRange, targetY),
            "L": (targetX - targetRange, targetY),
            "U": (targetX, targetY + targetRange),
            "D": (targetX, targetY - targetRange)
        }

        targetX, targetY = moves.get(player.direction, (targetX, targetY))

        self.aim(targetX, targetY)
    
    def getTargetRange(self, playerX, playerY, maxRange, counter = 0):
        if((abs(playerX - self.sprite.center_x) < maxRange) and (abs(playerY - self.sprite.center_y) < maxRange) and counter < 2):
            return self.getTargetRange(playerX, playerY, maxRange*0.8, counter + 1)
        
        return maxRange