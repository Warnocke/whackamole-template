import pygame,sys,random,math
from Costants import *
#use random.randrange(low, high). will use low number but not high (range should be low - high+1

def draw_grid():
    #draw horizontal lines
    for i in range(1,BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i*SQUARE_SIZE),
            (WIDTH,i*SQUARE_SIZE),
            LINE_WIDTH
        )
        #draw vert lines
    for i in range(1,BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i*SQUARE_SIZE,0),
            (i*SQUARE_SIZE,HEIGHT),
            LINE_WIDTH
        )

def set_screen():
    screen.fill("Light green")
    draw_grid()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def main():
    try:
        x,y=1,1
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        set_screen()
        screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = event.pos
                    distance = math.sqrt((mouse_x-x)**2+((mouse_y-y)**2))
                    if distance <= 32:
                        screen.fill("Light green")
                        draw_grid()
                        x = (random.randrange(0,20)*32+1)
                        y = (random.randrange(0,16)*32+1)
                        screen.blit(mole_image,mole_image.get_rect(topleft=(x,y)))
            pygame.display.flip()
            pygame.display.set_caption("Click tuah! Whack that mole!")
            clock.tick(60)
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
