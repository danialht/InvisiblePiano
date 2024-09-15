import pygame
import os

class Piano:
    def __init__(self):
        pygame.init()
        images_dir = os.path.join('assets', 'images')
        self.image = pygame.image.load(os.path.join(images_dir,'piano_keys.png'))
        self.window_width = 800
        self.window_height = 300
        
        self.image = pygame.transform.scale(self.image, (self.window_width, self.window_height))
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("My Pygame Window")
        self.init_loading_screen()
        self.IS_LOADING = True
        
        self.key_pressed = [False for _ in range(8)]
        self.rects = []
        for _ in range(8):
            new_rect = pygame.Surface((self.window_width // 8, self.window_height), pygame.SRCALPHA)
            new_rect.fill((255, 0, 0, 128))
            self.rects.append(new_rect)
        
    
    def press_key(self, index):
        self.key_pressed[index] = True
    
    def unpress_key(self, index):
        self.key_pressed[index] = False
    
    def init_loading_screen(self):
        font = pygame.font.Font(None, 36)
        self.screen.fill((255, 255, 255))
        # Define text
        text = "LOADING"
        text_color = (0, 150, 255)  # White
        text_surface = font.render(text, True, text_color)
        self.screen.blit(text_surface, (100, 100))
        pygame.display.flip()
             
    
    def update(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1

        # Fill the screen with a color (optional)
        self.screen.fill((255, 255, 255))


        # Draw shapes or images here (optional)
        self.screen.blit(self.image, (0, 0))
        
        
        for i in range(8):
            if self.key_pressed[i]:
                self.screen.blit(self.rects[i], (i * 100, 0))
        
        # Update the display
        pygame.display.flip()
        
        return 0


if __name__ == "__main__":
    x = Piano()
    while True:
        x.update()