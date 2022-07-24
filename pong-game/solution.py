import pygame
pygame.init()

# Constants 
WIDTH, HEIGHT = 700, 500
FPS = 60

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

class Paddle:
    COLOUR = WHITE

    # y coord will change based on user actions
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, window):
        pygame.draw.rectangle(window, self.COLOUR, (self.x, self.y, self.width, self.height))




def draw(window):
    window.fill(BLACK)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2, )

    while run:
        clock.tick(FPS)
        draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == '__main__':
    main()