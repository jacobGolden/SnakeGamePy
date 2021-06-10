import pygame
import sys
import random
from pygame.locals import *
pygame.init()
pygame.mixer.init()

# snake class
class Snake():
    # initializes the snake object
    def __init__(self):
        self.length = 3
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (255, 255, 255)
        self.score = 0

    # tracks the position of the snake head
    def get_head_position(self):
        return self.positions[0]

    # turning the snake
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    # snake movement
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        # attempt at making the walls solid --- NOT CURRENTLY WORKING
        # elif self.get_head_position() > GRID_WIDTH or self.get_head_position() > GRID_HEIGHT:
        #    self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # resets the game grid
    def reset(self):
        self.length = 3
        self.score = 0
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    # draw the snake on the grid -----> somewhere in this codeblock is where i'll add a pixelart head for the snake (snakeHead.png)
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (128, 128, 128), r, 1)

    # handle player input from the keyboard
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# food class
class Food():
    # initialize the food square on the grid
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()
    
    # randomize the next position where food appears
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT -1) * GRIDSIZE)
        # maybe this is where i make sure that the food can't spawn on the snake?
        

    # draw the food cube
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

# mushroom class
class Mushroom():
    # initialize the mushroom square on the grid
    def __init__(self):
        self.position = (0,0)
        self.color = (255,45,35)
        self.randomize_position()

    # randomize the next position where mushroom appears
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT -1) * GRIDSIZE)
    
    # draw the mushroom cube
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 255, 255), r, 1)

# blue mushroom class
class BlueShroom():
    # initialize the mushroom square on the grid
    def __init__(self):
        self.position = (0,0)
        self.color = (0, 0, 255)
        self.randomize_position()

    # randomize the next position where mushroom appears
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT -1) * GRIDSIZE)
    
    # draw the mushroom cube
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 255, 255), r, 1)

# black mushroom class
class BlackShroom():
    # initialize the mushroom square on the grid
    def __init__(self):
        self.position = (0,0)
        self.color = (0, 0, 0)
        self.randomize_position()

    # randomize the next position where mushroom appears
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT -1) * GRIDSIZE)
    
    # draw the mushroom cube
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 255, 255), r, 1)

# draw the grid whereon the game is played
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            # draws alternating light and dark shaded tiles for the grid background -> they match for now cause i'm testing solid color background
            if(x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (4, 71, 12), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (4, 71, 12), rr)

# game sound and music functions
def eatFoodSFX():
    eatFood = pygame.mixer.Sound("eatFood.wav")
    pygame.mixer.Sound.play(eatFood)

def eatShroomSFX():
    eatShroom = pygame.mixer.Sound("eatShroom.wav")
    pygame.mixer.Sound.play(eatShroom)

def themeMusic():
    pygame.mixer.music.load("happySnake.wav")
    pygame.mixer.music.play(-1)

# parameters for window size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

# font
myfont = pygame.font.SysFont("Comic Sans MS", 20)

# load images for sprites -> not currently working
snakeHeadSprite = pygame.image.load("snakeHead.png")
birdieSprite = pygame.image.load("food.png")
redShroomSprite = pygame.image.load("mushroom.png")
blueShroomSprite = pygame.image.load("blueShroom.png")
blackShroomSprite = pygame.image.load("blackShroom.png")

# directional movement
UP = (0,-1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# gameloop
def main():
    pygame.init()
    pygame.mixer.init()
    themeMusic()

    # runtime/speed
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    # game window
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    # objects
    snake = Snake()
    food = Food()
    redShroom = Mushroom()
    blueShroom = BlueShroom()
    blackShroom = BlackShroom()

    while(True):
        clock.tick(12)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        # snake eats food -> increase score and snake length
        if snake.get_head_position() == food.position:
            eatFoodSFX()
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        # snake eats mushroom -> decrease score but keep snake length
        elif snake.get_head_position() == redShroom.position:
            eatShroomSFX()
            snake.score -= 1
            redShroom.randomize_position()
        elif snake.get_head_position() == blueShroom.position:
            eatShroomSFX()
            snake.score -= 3
            blueShroom.randomize_position()
        elif snake.get_head_position() == blackShroom.position:
            eatShroomSFX()
            snake.score -= 5
            blackShroom.randomize_position()
        # draw snakes and mushrooms to the board
        snake.draw(surface)
        screen.blit(birdieSprite, food.position) # should produce food.png
        food.draw(surface)
        # screen.blit(redShroomSprite, redShroom.position) # should produce mushroom.png
        redShroom.draw(surface)
        # screen.blit(blueShroomSprite, blueShroom.position) # should produce blueShroom.png
        blueShroom.draw(surface)
        # screen.blit(blackShroomSprite, blackShroom.position) # should produce blackShroom.png
        blackShroom.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()

main()
