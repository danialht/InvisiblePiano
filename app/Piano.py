import os
import pygame


class Piano:
    """The Piano class would take care of the graphical
    piano which is displayed on a seperate window and
    it is responsible to play sounds and draw any
    graphical effect on the piano whenever a key is
    pressed.
    """

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 300

    def __init__(self):
        """Creates a window and calls appropriate initializer functions
        to initialize the loading screen, different sounds for different
        notes and the piano keys.
        """
        pygame.init()

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Invisible Piano")

        self.__init_loading_screen()
        self.__init_sounds()
        self.__init_keys()

    def __init_sounds(self):
        self.sounds = [
            pygame.mixer.Sound("./assets/sounds/C.wav"),
            pygame.mixer.Sound("./assets/sounds/C#.wav"),
            pygame.mixer.Sound("./assets/sounds/D.wav"),
            pygame.mixer.Sound("./assets/sounds/E.wav"),
            pygame.mixer.Sound("./assets/sounds/F.wav"),
            pygame.mixer.Sound("./assets/sounds/F#.wav"),
            pygame.mixer.Sound("./assets/sounds/G.wav"),
            pygame.mixer.Sound("./assets/sounds/C.wav"),
        ]

    def __init_keys(self):
        """Defines many different variables for different objectives,
        which are listed below:
        
        piano_image: the image of the piano which has to be drawn
        at every frame.
        
        key_pressed: list of booleans which indicate whether a key
        is pressed or not.
                        
        rects: list of eight 300px by 100px rectangles which are
        positioned on different keys and drawn whenever the is
        pressed.
        """
        images_dir = os.path.join("assets", "images")
        self.piano_image = pygame.image.load(os.path.join(images_dir, "piano_keys.png"))
        self.piano_image = pygame.transform.scale(
            self.piano_image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        )
        self.key_pressed = [False for _ in range(8)]
        self.rects = []
        for _ in range(8):
            new_rect = pygame.Surface(
                (self.WINDOW_WIDTH // 8, self.WINDOW_HEIGHT), pygame.SRCALPHA
            )
            new_rect.fill((255, 0, 0, 128))
            self.rects.append(new_rect)

    def press_key(self, index):
        """Changes the boolean status in key_pressed array to
        True and plays the sound. """
        self.key_pressed[index] = True
        self._play_sound(index)

    def unpress_key(self, index):
        """Changes the boolean status in key_pressed array to
        False. """
        self.key_pressed[index] = False

    def _play_sound(self, index):
        """Plays a specific note given by the index from the
        sounds array using pygame builting methods."""
        self.sounds[index].play()

    def __init_loading_screen(self):
        """Draws components of the loading screen on screen
        and updates the window.
        """
        font = pygame.font.Font(None, 36)
        self.screen.fill((255, 255, 255))
        text = "LOADING"
        text_color = (0, 150, 255)
        text_surface = font.render(text, True, text_color)
        self.screen.blit(text_surface, (100, 100))
        pygame.display.flip()

    def update(self):
        """Updates the whole screen. It first draws the piano
        image and every key which is pressed and updates the
        window.
        
        Returns 0 in case of successful update
        Returns 1 in case the user attempts to quit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1

        self.screen.blit(self.piano_image, (0, 0))

        # Draw colored rectangles on pressed keys
        for i in range(8):
            if self.key_pressed[i]:
                self.screen.blit(self.rects[i], (i * 100, 0))

        pygame.display.flip()
        return 0


if __name__ == "__main__":
    x = Piano()
    while True:
        x.update()
