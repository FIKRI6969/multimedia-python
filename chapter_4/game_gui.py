import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

image = pygame.image.load('test.png')
image = pygame.transform.scale(image, (100, 100))

sound = pygame.mixer.Sound('test.wav')
sound.play()

x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 5
    if x > 800:
        x = 0

    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    pygame.display.flip()

pygame.quit()
