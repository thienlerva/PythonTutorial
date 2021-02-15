import pygame
import os

pygame.init()
WIDTH, HEIGHT = 900, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Self Driving Car")
track = pygame.image.load(os.path.join('Assets', 'track1.png'))
car = pygame.image.load(os.path.join('Assets','tesla.png'))
car = pygame.transform.scale(car, (30, 60))

WHITE = (255, 255, 255)
FPS = 60

def draw_window():
    #window.fill((WHITE))
    window.blit(track, (0, 0))
    #window.blit(car, (0, 0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()