import pygame
pygame.init()

# Constants 
WIDTH, HEIGHT = 700, 500
FPS = 60
BALL_RADIUS = 7

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_WIDTH, PADDLE_HEIGHT = 16, 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

class Paddle:
    COLOUR = WHITE
    VELOCITY = 4

    # y coord will change based on user actions
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, window):
        pygame.draw.rect(window, self.COLOUR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY

class Ball:
    MAX_VELOCITY = 5
    COLOUR = WHITE
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0
    
    def draw(self, window):
        pygame.draw.circle(window, self.COLOUR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

def draw(window, paddles, ball):
    window.fill(BLACK)

    # Draw paddles
    for paddle in paddles:
        paddle.draw(window)

    # Draw ball
    ball.draw(window)
    
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 0:
            pygame.draw.rect(window, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and HEIGHT - left_paddle.y - left_paddle.height  >= left_paddle.VELOCITY:
        left_paddle.move(up=False)
        
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and HEIGHT - right_paddle.y - right_paddle.height  >= right_paddle.VELOCITY:
        right_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    while run:
        clock.tick(FPS)
        draw(screen, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
    pygame.quit()

if __name__ == '__main__':
    main()