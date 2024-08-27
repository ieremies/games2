#!/usr/bin/env python3

import pygame
import sys


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100

        self.width = 50
        self.height = 50

        self.color = (255, 0, 0)
        self.rect = (self.x, self.y, self.width, self.height)

        self.vel = 3

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

    def update(self, display):
        # chama para processar qualquer movimento
        self.move()
        # redesenha na tela
        pygame.draw.rect(display, self.color, self.rect)


# ====================================================================================


pygame.init()  # inicializa a biblioteca

WIDTH = 350
HEIGHT = 650
display = pygame.display.set_mode((WIDTH, HEIGHT))  # inicia a tela
pygame.display.set_caption("Nome do Meu Jogo")

clock = pygame.time.Clock()  # inicia o relógio

p = Player()  # cria um jogador

while True:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # background
    display.fill((255, 255, 255))

    # Processa o jogador
    p.update(display)

    pygame.display.update()  # atualiza a tela

    clock.tick(60)  # 60 frames por segundo
