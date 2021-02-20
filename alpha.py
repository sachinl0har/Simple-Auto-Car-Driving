import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
carX = 150
carY = 300
focalDis = 25
camX_offset = 0
camY_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    camX = carX + camX_offset + 15
    camY = carY + camY_offset + 15
    up_px = window.get_at((camX, camY - focalDis))[0]
    down_px = window.get_at((camX, camY + focalDis))[0]
    right_px = window.get_at((camX + focalDis, camY))[0]
    print(up_px, right_px, down_px)
    # Take Turn
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        camX_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        carX = carX + 30
        camX_offset = 0
        camY_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        carY = carY + 30
        camY_offset = 0
        camX_offset = 30
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        carX = carX + 30
        camX_offset = 0
        car = pygame.transform.rotate(car, 90)
    # Drive
    if direction == 'up' and up_px == 255:
        carY = carY - 2
    elif direction == 'right' and right_px == 255:
        carX = carX + 2
    elif direction == 'down' and down_px == 255:
        carY = carY + 2
    window.blit(track, (0, 0))     #blit = Block Image Transfer
    window.blit(car, (carX, carY))
    pygame.draw.circle(window, (0, 255, 0), (camX, camY), 5, 5)
    pygame.display.update()