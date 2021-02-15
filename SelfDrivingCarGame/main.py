import pygame
import os

pygame.init()
WIDTH, HEIGHT = 1200, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Self Driving Car")
track = pygame.image.load(os.path.join('Assets', 'track5.png'))
car = pygame.transform.scale(pygame.image.load(os.path.join('Assets','tesla.png')), (30, 60))

GREEN = (0, 255, 0)
FPS = 60
VELOCITY = 2
focal_dis = 25
cam_x_change = 0
cam_y_change = 0
direction = 'up'

def draw_window(x, y, car, cam_x, cam_y):

    window.blit(track, (0, 0))
    window.blit(car, (x, y))
    pygame.draw.circle(window, GREEN, (cam_x, cam_y), 5, 5)

    pygame.display.update()

def main(x, y, car):
    clock = pygame.time.Clock()
    running = True
    global direction
    global cam_x_change
    global cam_y_change

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        cam_x = x + 15 + cam_x_change
        cam_y = y + 15 + cam_y_change
        up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
        down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
        right_px = window.get_at((cam_x + focal_dis, cam_y))[0]

        print(up_px, right_px)
        # change direction
        if direction == 'up' and up_px != 255 and right_px == 255:
            direction = 'right'
            cam_x_change = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'right' and right_px != 255 and down_px == 255:
            direction = 'down'
            x += 30
            cam_x_change = 0
            cam_y_change = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'down' and down_px != 255 and right_px == 255:
            direction = 'right'
            y += 30
            cam_x_change = 30
            cam_y_change = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'right' and right_px != 255 and up_px == 255:
            direction = 'up'
            x += 30
            cam_x_change = 0
            car = pygame.transform.rotate(car, 90)

        # Drive
        if direction == 'up' and up_px == 255:
            y -= VELOCITY
        elif direction == 'right' and right_px == 255:
            x += VELOCITY
        elif direction == 'down' and down_px == 255:
            y += VELOCITY

        draw_window(x, y, car, cam_x, cam_y)

    pygame.quit()

if __name__ == "__main__":
    car_x, car_y = 155, 300
    car = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'tesla.png')), (30, 60))
    main(car_x, car_y, car)


