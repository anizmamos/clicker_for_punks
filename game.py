import pygame
import random
import time
pygame.init()
size = width, height = 800, 600
ekran = pygame.display.set_mode(size)
pygame.display.set_caption("Clicker for punks")
ekran.fill((255, 255, 255))


def game_intro(score, k):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score += random.randint(-25, 25) + k
        ekran.fill(pygame.Color("white"), (0, 0, 900, 900))
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font(None, 50)
        text = font.render('score: ' + str(score), 1, (50, 50, 100))
        ekran.blit(text, (50, 50))
        text2 = font.render("Улучшение(" + str(100 * k) + ") ->", 1, (50, 50, 100))
        ekran.blit(text2, (50, 100))
        text2 = font.render("Осталось:" + str(score + 500), 1, (50, 50, 100))
        ekran.blit(text2, (50, 150))
        if 800 > mouse[0] > 0 and 600 > mouse[1] > 500:
            pygame.draw.rect(ekran, (100, 100, 200), (0, 500, 800, 100))
            if pygame.mouse.get_pressed()[0]:
                score += random.randint(-25, 25) + k
                time.sleep(0.1)
                ekran.fill(pygame.Color("white"), (0, 0, 300, 300))
        else:
            pygame.draw.rect(ekran, (0, 0, 100), (0, 500, 800, 100))
        if 800 > mouse[0] > 400 and 500 > mouse[1] > 0:
            pygame.draw.rect(ekran, (200, 100, 100), (400, 0, 500, 500))
            if pygame.mouse.get_pressed()[0]:
                k += 1
                score -= 100 * k
                ekran.fill(pygame.Color("white"), (0, 0, 300, 300))
                time.sleep(0.1)
        else:
            pygame.draw.rect(ekran, (100, 0, 0), (400, 0, 500, 500))

        if score < -500:
            ekran.fill(pygame.Color("black"), (0, 0, 900, 500))
            text3 = font.render("Вы проиграли!", 1, (200, 0, 0))
            ekran.blit(text3, (250, 250))
            text4 = font.render("Заново", 1, (200, 0, 0))
            ekran.blit(text4, (320, 450))
            if 800 > mouse[0] > 0 and 600 > mouse[1] > 500:
                pygame.draw.rect(ekran, (100, 100, 200), (0, 500, 800, 100))
                if pygame.mouse.get_pressed()[0]:
                    score, k = 0, 0
        pygame.display.update()


game_intro(0, 0)
pygame.display.flip()
pygame.quit()
