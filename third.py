#!/usr/bin/env python3


#!/usr/bin/env python3

import pygame
import sys


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100

        self.width = 50
        self.height = 50

        self.image = pygame.image.load("dvd.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.vel = (0.5, 0.5)

    def move(self, display):
        # atualiza posição com cada componente da velocidade
        self.x += self.vel[0]
        self.y += self.vel[1]

        # inverte a velocidade se atingir as bordas
        if self.x <= 0 or self.x >= display.get_width() - self.width:
            self.vel = (-self.vel[0], self.vel[1])
        if self.y <= 0 or self.y >= display.get_height() - self.height:
            self.vel = (self.vel[0], -self.vel[1])

        self.rect = (self.x, self.y, self.width, self.height)

    def update(self, display):
        # chama para processar qualquer movimento
        self.move(display)
        # redesenha na tela
        # pygame.draw.rect(display, self.color, self.rect)
        display.blit(self.image, (self.x, self.y))


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
