# entidades/projetil.py
import pygame
import math
from config import *

class Projetil:
    def __init__(self, x, y, alvo_x, alvo_y, dano, imagem):
        self.x = x
        self.y = y
        self.alvo_x = alvo_x
        self.alvo_y = alvo_y
        self.dano = dano
        self.imagem = imagem 
        self.velocidade = 15 
        self.atingiu = False 

        dx = alvo_x - x
        dy = alvo_y - y
        distancia = math.hypot(dx, dy)
        if distancia == 0: 
            self.vel_x = 0
            self.vel_y = 0
        else:
            self.vel_x = (dx / distancia) * self.velocidade
            self.vel_y = (dy / distancia) * self.velocidade

        angulo = math.degrees(math.atan2(-dy, dx))
        self.imagem = pygame.transform.rotate(self.imagem, angulo)
        self.rect = self.imagem.get_rect(center=(self.x, self.y))

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.center = (int(self.x), int(self.y)) 
        
        if self.x < -100 or self.x > TAMANHO_TELA[0] + 100 or self.y < -100 or self.y > TAMANHO_TELA[1] + 100:
            return True 
        return False

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)
