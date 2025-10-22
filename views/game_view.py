import arcade
from managers.input_manager import InputManager
from entities.player import Player
from entities.blinky import Blinky
from entities.pinky import Pinky

class GameView(arcade.View):
    """Vue principale du jeu."""

    def __init__(self):
        super().__init__()
        #self.input_manager = InputManager()
        self.frame = 0

        self.background = arcade.load_texture("assets/background/space.jpeg")

        self.player = Player(self.window)
        self.blinky = Blinky(self.window)
        self.pinky = Pinky(self.window)

        self.sprite_list = arcade.SpriteList()
        self.sprite_list.extend([self.player.sprite, self.blinky.sprite, self.pinky.sprite])


        
    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, self.window.width, self.window.height),
        )

        self.sprite_list.draw()

    def on_update(self, dt):
        self.frame = self.frame + 1 % 60
        self.player.animate(dt)
        self.blinky.animate(dt)
        self.pinky.animate(dt)

        self.player.forward()
        self.blinky.move(self.player, self.frame)
        self.pinky.move(self.player, self.frame)
        

    def on_key_press(self, key, modifiers):
        #self.input_manager.on_key_press(key)
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        #self.input_manager.on_key_release(key)
        pass