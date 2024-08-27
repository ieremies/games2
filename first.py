#!/usr/bin/env python3

import pygame
import sys

pygame.init()  # inicializa a biblioteca

WIDTH = 350
HEIGHT = 650
display = pygame.display.set_mode((WIDTH, HEIGHT))  # inicia a tela
pygame.display.set_caption("Nome do Meu Jogo")

clock = pygame.time.Clock()  # inicia o relógio

x = 50
y = 50
while True:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Você soltou a tecla pra cima!")

    # background
    display.fill((0, 0, 0))
    # Desenha retangulo vermelho
    pygame.draw.rect(display, (255, 0, 0), (x, y, 50, 50))

    pygame.display.update()  # atualiza a tela

    clock.tick(10)  # 60 frames por segundo
