import arcade
from managers.input_manager import InputManager
from entities.player import Player
from entities.blinky import Blinky
from entities.pinky import Pinky
from entities.inky import Inky
from entities.clyde import Clyde
from entities.dot import Dot

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
        self.clyde = Clyde(self.window)

        self.phantoms = [self.blinky, self.pinky, self.inky, self.clyde]
        self.dots = [Dot(self.window, "dot1"), Dot(self.window, "dot2")]


        self.phantom_sprite_list = arcade.SpriteList()
        self.phantom_sprite_list.extend([self.blinky.sprite, self.pinky.sprite, self.inky.sprite, self.clyde.sprite])

        self.player_sprite_list = arcade.SpriteList()
        self.player_sprite_list.extend([self.player.sprite] + [dot.sprite for dot in self.dots])

        self.game_over = False
        


        
    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, self.window.width, self.window.height),
        )


        self.player_sprite_list.draw()
        self.phantom_sprite_list.draw()
        arcade.draw_text(f"Score {self.player.score}", 50, self.window.height-50, arcade.color.WHITE, 40)

    def on_update(self, dt):
        self.frame = self.frame + 1 % 60

        for phantom in self.phantoms:
            phantom.animate(dt)
        
        self.player.animate(dt)
        for dot in self.dots:
            dot.spawn(self.window) 
        
        if not self.game_over:
            self.player.move()
            self.blinky.move(self.player, self.frame)
            self.pinky.move(self.player, self.frame)
            self.inky.move(self.player, self.frame, self.phantoms)
            self.clyde.move(self.player, self.frame)

        if(arcade.check_for_collision_with_list(self.player.sprite, self.phantom_sprite_list)):
            self.game_over = True

        for dot in self.dots:
            if arcade.check_for_collision(self.player.sprite, dot.sprite):
                if dot.sprite.visible:
                    self.setScore(self.player.score + 1)
                    dot.despawn()

        

    def on_key_press(self, key, modifiers):
        #self.input_manager.on_key_press(key)
        self.player.on_key_press(key)
        if self.game_over:
            newGame = GameView()
            self.window.show_view(newGame)

    def on_key_release(self, key, modifiers):
        #self.input_manager.on_key_release(key)
        pass

    def setScore(self, score):
        self.player.score = score
        for phantom in self.phantoms: phantom.speed += 0.1
        
        if score % 4 == 0:
            self.player.speed += 0.4
            for phantom in self.phantoms: phantom.speed += 0.1