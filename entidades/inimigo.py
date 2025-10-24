# entidades/inimigo.py
import pygame
from config import *

class Inimigo:
    def __init__(self, caminho):
        self.caminho = caminho
        self.x, self.y = self.caminho[0]
        self.indice = 0
        self.vel = 2
        
        self.largura = 32
        self.altura = 32
        
        self.imagem_original = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
        VERDE_INIMIGO = (0, 100, 0)
        self.imagem_original.fill(VERDE_INIMIGO)
        pygame.draw.rect(self.imagem_original, PRETO, (0, 0, self.largura, self.altura), 1)

        self.imagem = pygame.transform.scale(self.imagem_original, (self.largura, self.altura))
        self.rect = self.imagem.get_rect(topleft=(self.x, self.y))
        
        self.vida_max = 100
        self.vida = self.vida_max

    def mover(self):
        if self.indice + 1 < len(self.caminho):
            alvo_x, alvo_y = self.caminho[self.indice + 1]
            dx = alvo_x - self.x
            dy = alvo_y - self.y
            distancia = (dx**2 + dy**2) ** 0.5
            
            if distancia < self.vel:
                self.x, self.y = alvo_x, alvo_y
                self.indice += 1
            else:
                self.x += dx / distancia * self.vel
                self.y += dy / distancia * self.vel
            
            self.rect.topleft = (int(self.x), int(self.y))
            return False
        else:
            return True

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

        if self.vida <= 0:
            return

        vida_ratio = self.vida / self.vida_max
        barra_largura = self.largura
        barra_altura = 5
        barra_x = self.x
        barra_y = self.y - 8

        if vida_ratio > 0.6:
            cor_vida = VERDE
        elif vida_ratio > 0.3:
            cor_vida = AMARELO
        else:
            cor_vida = VERMELHO

        pygame.draw.rect(tela, PRETO, (barra_x, barra_y, barra_largura, barra_altura))
        pygame.draw.rect(tela, cor_vida, (barra_x, barra_y, barra_largura * vida_ratio, barra_altura))
