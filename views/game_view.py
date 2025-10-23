import arcade
from managers.input_manager import InputManager
from entities.player import Player
from entities.blinky import Blinky
from entities.pinky import Pinky
from entities.inky import Inky

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
        self.inky = Inky(self.window)

        self.phantoms = [self.blinky, self.pinky]


        self.phantom_sprite_list = arcade.SpriteList()
        self.phantom_sprite_list.extend([self.blinky.sprite, self.pinky.sprite, self.inky.sprite])

        self.player_sprite_list = arcade.SpriteList()
        self.player_sprite_list.extend([self.player.sprite])

        self.game_over = False
        


        
    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, self.window.width, self.window.height),
        )


        self.player_sprite_list.draw()
        self.phantom_sprite_list.draw()

    def on_update(self, dt):
        self.frame = self.frame + 1 % 60

        for phantom in self.phantoms:
            phantom.animate(dt)
        
        self.player.animate(dt)
        
        if self.game_over == False:
            self.player.move()
            self.blinky.move(self.player, self.frame)
            self.pinky.move(self.player, self.frame)
            self.inky.move(self.player, self.frame, self.phantoms)

        if(arcade.check_for_collision_with_list(self.player.sprite, self.phantom_sprite_list)):
            self.game_over = True
        

    def on_key_press(self, key, modifiers):
        #self.input_manager.on_key_press(key)
        self.player.on_key_press(key)
        if self.game_over:
            newGame = GameView()
            self.window.show_view(newGame)

    def on_key_release(self, key, modifiers):
        #self.input_manager.on_key_release(key)
        pass