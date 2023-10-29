"""Scene objects for making games with PyGame."""

import pygame
import rgbcolors
import os
from enemy import Enemy, direction, down
from player import Player

# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


class Scene:
    """Base class for making PyGame Scenes."""

    def __init__(self, screen, background_color, soundtrack=None):
        """Scene initializer"""
        self.screen = screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(background_color)
        self.frame_rate = 60
        self._is_valid = True
        self.soundtrack = soundtrack
        self._render_updates = None

    def draw(self):
        """Draw the scene."""
        self.screen.blit(self.background, (0, 0))

    def process_event(self, event):
        """Process a game event by the scene."""
        # This should be commented out or removed since it generates a lot of noise.
        # print(str(event))
        if event.type == pygame.QUIT:
            print("Good Bye!")
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Bye bye!")
            self._is_valid = False

    def is_valid(self):
        """Is the scene valid? A valid scene can be used to play a scene."""
        return self._is_valid

    def render_updates(self):
        """Render all sprite updates."""

    def update_scene(self):
        """Update the scene state."""
        pygame.display.update()

    def start_scene(self):
        """Start the scene."""
        if self.soundtrack:
            try:
                pygame.mixer.music.load(self.soundtrack)
                pygame.mixer.music.set_volume(0.2)
            except pygame.error as pygame_error:
                print("Cannot open the mixer?")
                print('\n'.join(pygame_error.args))
                raise SystemExit("broken!!") from pygame_error
            pygame.mixer.music.play(-1)

    def end_scene(self):
        """End the scene."""
        if self.soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

    def frame_rate(self):
        """Return the frame rate the scene desires."""
        return self.frame_rate


class PressAnyKeyToExitScene(Scene):
    """Empty scene where it will invalidate when a key is pressed."""

    def process_event(self, event):
        """Process game events."""
        # TODO: Have the super/parent class process the event first before
        # processing the event yourself.
        # TOOD: If the event type is a keydown event, set self._is_valid to False.


class PolygonTitleScene(PressAnyKeyToExitScene):
    """Scene with a title string and a polygon."""

    def __init__(
        self,
        screen,
        title,
        title_color=rgbcolors.ghostwhite,
        title_size=72,
        background_color=rgbcolors.papaya_whip,
        soundtrack=None,
    ):
        """Initialize the scene."""
        # TODO: Have the super/parent class initialized
        # TODO: Ask pygame for the default font at title_size size. Use the font to render the string title and assign this to an instance variable named self._title in the color title_color.
        # TODO: Ask pygame for the default font at 18 point size. Use the font to render the string 'Press any key.' in the color black. Assign the rendered text to an instance variable named self._press_any_key.

    def draw(self):
        """Draw the scene."""
        # TODO: Have the super/parent class draw first before
        # drawing yourself.
        # TODO: Draw a 100 pixel by 100 pixel rectangle that has it's center located 100 pixels below the center of the window.
        # TODO: Blit the title text to the center of the window.
        # TODO: Blit the press any key message to the bottom of the window. The text should be centered horizontally and be 50 pixels above the bottom edge of the window.

class TitleScreen(Scene):
    def __init__(self, screen, soundtrack = None):
        self._main_dir = os.path.dirname(__file__)
        self._data_dir = os.path.join(self._main_dir, "data")
        self.screen = screen
        self.soundtrack = soundtrack
        self.valid = True
        self.title_text = "SPACE"
        self.title_text_2 = "INVADERS"
        pygame.display.set_caption("Space Invaders")
        self.frames = 60
        self.background = pygame.image.load(os.path.join(self._data_dir, "index.jpg"))
        self.background = pygame.transform.scale(self.background, (600, 600))
        self.option_list = []
        self.clock = pygame.time.Clock()
        self.next_key = "game"

    def options(self):
        my_font = os.path.join(self._data_dir, "Cabal-w5j3.ttf")
        title_f = os.path.join(self._data_dir, "Freedom-10eM.ttf")
        font = pygame.font.Font(my_font, 40)
        title_font = pygame.font.Font(title_f, 70)
        start_text = "Play Game"
        leave_text = "Quit"
        option_1 = font.render(start_text, True, rgbcolors.gray)
        option_2 = font.render(start_text, True, rgbcolors.white)
        option_3 = font.render(leave_text, True, rgbcolors.gray)
        option_4 = font.render(leave_text, True, rgbcolors.white)
        title = title_font.render(self.title_text, True, rgbcolors.gray)
        title_2 = title_font.render(self.title_text_2, True, rgbcolors.gray)
        self.option_list.append(option_1)
        self.option_list.append(option_2)
        self.option_list.append(option_3)
        self.option_list.append(option_4)
        self.option_list.append(title)
        self.option_list.append(title_2)

    def run(self):
        self.options()
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.option_list[4], (175, 75))
        self.screen.blit(self.option_list[5], (130, 130))
        while self.valid:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN and 200 <= mouse_pos[0] <= 425 and 360 <= mouse_pos[1] <= 385:
                    #Clicked Play
                    #Go to next screen
                    self.valid = False
                elif event.type == pygame.MOUSEBUTTONDOWN and 265 <= mouse_pos[0] <= 350 and 410 <= mouse_pos[1] <= 460:
                    #Clicked Quit
                    self.next_key = "quit"
                    self.valid = False
            
            if 200 <= mouse_pos[0] <= 425 and 360 <= mouse_pos[1] <= 385:
                text_1 = self.option_list[1]
            else:
                text_1 = self.option_list[0]
            
            if 265 <= mouse_pos[0] <= 350 and 410 <= mouse_pos[1] <= 460:
                text_2 = self.option_list[3]
            else:
                text_2 = self.option_list[2]
            self.screen.blit(text_1, (200, 350))
            self.screen.blit(text_2, (265, 400))
            pygame.display.update()
            self.clock.tick(self.frames)
    
class WinScreen(Scene):
    def __init__(self, screen, score, soundtrack = None):
        self._main_dir = os.path.dirname(__file__)
        self._data_dir = os.path.join(self._main_dir, "data")
        self.screen = screen
        self.soundtrack = soundtrack
        self.valid = True
        self.title = "Level"
        self.title_2 = "Cleared"
        self.flavor = "Next level starting"
        self.score = score
        self.score_display = f"Score: {self.score}"
        self.used_font = None
        pygame.display.set_caption("Space Invaders")
        self.option_list = []
        self.last_loaded = pygame.time.get_ticks()
        self.load_cooldown = 500
        self.frames = 60
        self.background = pygame.image.load(os.path.join(self._data_dir, "space-stars-texture-sololos.jpg"))
        self.background = pygame.transform.scale(self.background, (600, 600))
        self.clock = pygame.time.Clock()
        self.next_key = "game"
    
    def options(self):
        my_font = os.path.join(self._data_dir, "Cabal-w5j3.ttf")
        title_f = os.path.join(self._data_dir, "Freedom-10eM.ttf")
        text_font = pygame.font.Font(my_font, 40)
        self.used_font = text_font
        title_font = pygame.font.Font(title_f, 70)
        option_1 = text_font.render(self.flavor, True, rgbcolors.gray)
        option_2 = text_font.render(self.score_display, True, rgbcolors.gray)
        option_3 = title_font.render(self.title, True, rgbcolors.gray)
        option_4 = title_font.render(self.title_2, True, rgbcolors.gray)
        self.option_list.append(option_1)
        self.option_list.append(option_2)
        self.option_list.append(option_3)
        self.option_list.append(option_4)
    
    def set_flavor(self, count):
        dots = ""
        for _ in range(count):
            dots = dots + "."
        self.flavor = f"Next level starting{dots}"
        self.option_list[0] = self.used_font.render(self.flavor, True, rgbcolors.gray)
    
    def load_buffer(self):
        current = pygame.time.get_ticks()
        if current - self.last_loaded >= self.load_cooldown:
            self.last_loaded = current
            return True
        return False
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.option_list[2], (185, 50)) # Level
        self.screen.blit(self.option_list[3], (135, 115)) # Cleared
        self.screen.blit(self.option_list[0], (120, 300)) # Loading
        self.screen.blit(self.option_list[1], (180, 450)) # Score

    def run(self):
        count = 0
        finish = 0
        self.options()
        self.draw()
        while finish < 11:
            if self.load_buffer():
                count = count + 1
                if count > 3:
                    count = 0
                self.set_flavor(count)
                self.draw()
                finish = finish + 1
            pygame.display.update()
            self.clock.tick(self.frames)
        self.active = False

class LoseScreen(Scene):
    def __init__(self, screen, score, soundtrack = None):
        self._main_dir = os.path.dirname(__file__)
        self._data_dir = os.path.join(self._main_dir, "data")
        self.screen = screen
        self.soundtrack = soundtrack
        self.valid = True
        self.title = "You Died"
        self.score = score
        self.score_display = f"Score is {self.score}:"
        self.play_again = "Play again"
        self.quit = "Quit"
        self.number_1 = f"#1: {str(10000)} BOB"
        self.number_2 = f"#2: {str(5000)} HAM" #Implement high scores and player name input
        self.number_3 = f"#3: {str(1000)} GEM"
        self.used_font = None
        pygame.display.set_caption("Space Invaders")
        self.last_loaded = pygame.time.get_ticks()
        self.load_cooldown = 500
        self.option_list = []
        self.background = pygame.image.load(os.path.join(self._data_dir, "space-stars-texture-sololos.jpg"))
        self.background = pygame.transform.scale(self.background, (600, 600))
        self.frames = 60
        self.clock = pygame.time.Clock()
        self.next_key = "game"
    
    def options(self):
        my_font = os.path.join(self._data_dir, "Cabal-w5j3.ttf")
        title_f = os.path.join(self._data_dir, "Freedom-10eM.ttf")
        text_font = pygame.font.Font(my_font, 40)
        self.used_font = text_font
        title_font = pygame.font.Font(title_f, 70)
        option_1 = text_font.render(self.score_display, True, rgbcolors.gray)
        option_2 = title_font.render(self.title, True, rgbcolors.gray)
        option_3 = text_font.render(self.play_again, True, rgbcolors.gray)
        option_4 = text_font.render(self.quit, True, rgbcolors.gray)
        option_5 = text_font.render(self.number_1, True, rgbcolors.gray)
        option_6 = text_font.render(self.number_2, True, rgbcolors.gray)
        option_7 = text_font.render(self.number_3, True, rgbcolors.gray)
        option_8 = text_font.render(self.play_again, True, rgbcolors.white)
        option_9 = text_font.render(self.quit, True, rgbcolors.white)
        self.option_list.append(option_1)
        self.option_list.append(option_2)
        self.option_list.append(option_3)
        self.option_list.append(option_4)
        self.option_list.append(option_5)
        self.option_list.append(option_6)
        self.option_list.append(option_7)
        self.option_list.append(option_8)
        self.option_list.append(option_9)
    
    def get_name(self, letters):
        stutter = True
        if len(letters) > 3:
            letters = letters[0:3]
        if stutter:
            self.score_display = f"Score is {self.score}: {letters}_"
            self.option_list[0] = self.used_font.render(self.score_display, True, rgbcolors.gray)
            stutter = False
        else:
            self.score_display = f"Score is {self.score}: {letters}"
            self.option_list[0] = self.used_font.render(self.score_display, True, rgbcolors.gray)
            stutter = True
    
    def load_buffer(self):
        current = pygame.time.get_ticks()
        if current - self.last_loaded >= self.load_cooldown:
            self.last_loaded = current
            return True
        return False

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.option_list[0], (150, 200))
        self.screen.blit(self.option_list[1], (130, 50))
        self.screen.blit(self.option_list[2], (200, 450)) # Play Again
        self.screen.blit(self.option_list[3], (265, 500)) # Quit
        self.screen.blit(self.option_list[4], (175, 240))
        self.screen.blit(self.option_list[5], (175, 280))
        self.screen.blit(self.option_list[6], (175, 320))
    
    def run(self):
        self.options()
        self.draw()

        while self.valid:
            mouse_pos = pygame.mouse.get_pos()
            if self.load_buffer():
                for event in pygame.event.get():
                    self.get_name("k")
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and 200 <= mouse_pos[0] <= 415 and 460 <= mouse_pos[1] <= 490:
                    #Clicked Play
                    #Go to next screen
                    self.valid = False
                elif event.type == pygame.MOUSEBUTTONDOWN and 265 <= mouse_pos[0] <= 350 and 510 <= mouse_pos[1] <= 540:
                    #Clicked Quit
                    self.next_key = "quit"
                    self.valid = False
            
            if 200 <= mouse_pos[0] <= 415 and 460 <= mouse_pos[1] <= 490:
                text_1 = self.option_list[7]
            else:
                text_1 = self.option_list[2]
            
            if 265 <= mouse_pos[0] <= 350 and 510 <= mouse_pos[1] <= 540:
                text_2 = self.option_list[8]
            else:
                text_2 = self.option_list[3]
            self.draw()
            self.screen.blit(text_1, (200, 450))
            self.screen.blit(text_2, (265, 500))
            pygame.display.update()
            self.clock.tick(self.frames)

class GameScreen(Scene):
    def __init__(self, screen, score, lives, level, soundtrack = None):
        self._main_dir = os.path.dirname(__file__)
        self._data_dir = os.path.join(self._main_dir, "data")
        self.screen = screen
        self.soundtrack = soundtrack
        self.valid = True
        self.score = score
        self.score_display = f"{self.score}"
        self.lives = lives
        self.lives_display = "Lives: "
        self.lives_image = pygame.image.load(os.path.join(self._data_dir, "big_boss1.png"))
        self.lives_image = pygame.transform.scale(self.lives_image, (24, 24))
        self.level = level
        self.level_display = f"Level {self.level}"
        self.used_font = None
        self.background = pygame.Surface(self.screen.get_size())
        self.move_down_buffer = pygame.time.get_ticks()
        self.move_down_cooldown = 1000
        self.option_list = []
        self.enemy_list = []
        self.clock = pygame.time.Clock()
        self.frames = 60
        self.next_key = "win"
    
    def make_enemies(self):
        self.enemy_list.append(Enemy(self.screen, (50, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (100, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (150, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (200, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (250, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (300, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (350, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (400, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (450, 50), 0))
        self.enemy_list.append(Enemy(self.screen, (500, 50), 0))

        self.enemy_list.append(Enemy(self.screen, (50, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (100, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (150, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (200, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (250, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (300, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (350, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (400, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (450, 100), 1))
        self.enemy_list.append(Enemy(self.screen, (500, 100), 1))

        self.enemy_list.append(Enemy(self.screen, (50, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (100, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (150, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (200, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (250, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (300, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (350, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (400, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (450, 150), 2))
        self.enemy_list.append(Enemy(self.screen, (500, 150), 2))

    def switch_buffer(self):
        global down
        current = pygame.time.get_ticks()
        if current - self.move_down_buffer >= self.move_down_cooldown:
            self.move_down_buffer = current
            return True
        return False
    
    def options(self):
        my_font = os.path.join(self._data_dir, "Cabal-w5j3.ttf")
        text_font = pygame.font.Font(my_font, 40)
        self.used_font = text_font
        option_1 = text_font.render(self.score_display, True, rgbcolors.gray)
        option_2 = text_font.render(self.lives_display, True, rgbcolors.gray)
        option_3 = text_font.render(self.level_display, True, rgbcolors.gray)
        self.option_list.append(option_1)
        self.option_list.append(option_2)
        self.option_list.append(option_3)
    
    def draw(self):
        self.screen.fill(rgbcolors.black)
        self.screen.blit(self.option_list[0], (10, 10))
        self.screen.blit(self.option_list[1], (10, 560))
        self.screen.blit(self.option_list[2], (260, 10))

        for lives in range(self.lives):
            self.screen.blit(self.lives_image, ((lives + 1) * 26 + 87, 570))
    
    def lose_life(self):
        self.lives = self.lives - 1
        if self.lives == 0:
            self.next_key = "lose"
            self.valid = False
            return
        else:
            return False
        
    def update_score(self, score):
        self.score = self.score + score
        self.score_display = f"{self.score}"
        self.option_list[0] = self.used_font.render(self.score_display, True, rgbcolors.gray)
    
    def run(self):
        my_player = Player(self.screen)
        self.make_enemies()
        self.options()
        global down
        global direction
        while self.valid:
            for event in pygame.event.get():
                if event == pygame.K_ESCAPE:
                    self.valid = False
            my_player.handle_keys()
            my_player.shoot()
            self.draw()
            my_player.draw()
            for index, enemy in enumerate(self.enemy_list):
                if down:
                    for ship in self.enemy_list:
                        ship.move_down()
                    for bot in self.enemy_list[0:index]:
                        bot.last_move = 0
                        bot.move_down()
                        bot.smart_move_down()
                    down = False
                if enemy.move() and self.switch_buffer():
                    if direction is True:
                        direction = False
                        for enemy in self.enemy_list[0:index]:
                            enemy.smart_move()
                    else:
                        direction = True
                        for enemy in self.enemy_list[0:index]:
                            enemy.smart_move()
                    down = True
                if enemy.check_collision(my_player.bullet_list):
                    self.enemy_list.pop(index) # Death image and sound needed
                    self.update_score(100)
            for bullet in my_player.bullet_list:
                bullet.travel()
            for enemy in self.enemy_list:
                enemy.shoot()
                for bullet in enemy.bullet_list:
                    bullet.enemy_travel()
                    if my_player.check_tangibility():
                        if my_player.check_collision(enemy.bullet_list):
                            self.lose_life()
                            my_player.reset()
            
            if my_player.check_tangibility:
                if my_player.check_collision(self.enemy_list):
                    self.lose_life()
                    my_player.reset()



            pygame.display.update()
            self.clock.tick(60)

            if not self.enemy_list:
                self.update_score(3000)
                self.level = self.level + 1
                self.valid = False
