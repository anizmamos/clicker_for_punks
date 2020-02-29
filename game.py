import pygame
import random
import time
pygame.init()
size = width, height = 800, 600
ekran = pygame.display.set_mode(size)
ekran.fill((255, 255, 255))


def game_intro(score, k):
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font(None, 50)
        text = font.render(str(score), 1, (50, 50, 100))
        ekran.blit(text, (50, 50))
        if 800 > mouse[0] > 0 and 600 > mouse[1] > 500:
            pygame.draw.rect(ekran, (100, 100, 200), (0, 500, 800, 100))
            if pygame.mouse.get_pressed()[0]:
                score += random.randint(-25, 25) * k
                time.sleep(0.1)
                ekran.fill(pygame.Color("white"), (0, 0, 300, 300))
        else:
            pygame.draw.rect(ekran, (0, 0, 100), (0, 500, 800, 100))
        if 800 > mouse[0] > 400 and 500 > mouse[1] > 0:
            pygame.draw.rect(ekran, (200, 100, 100), (400, 0, 500, 500))
            if pygame.mouse.get_pressed()[0]:
                k += 1
                score -= 100* k
                ekran.fill(pygame.Color("white"), (0, 0, 300, 300))
                time.sleep(0.1)
        else:
            pygame.draw.rect(ekran, (100, 0, 0), (400, 0, 500, 500))
        pygame.display.update()


game_intro(0, 1)
pygame.display.flip()
pygame.quit()
