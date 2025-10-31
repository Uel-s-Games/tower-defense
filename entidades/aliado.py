
import math
import pygame
from entidades.projetil import Projetil
from config import * 

class Aliado:
    def __init__(self, x, y, imagem, dano=20, index_loja=0):
        self.x = x
        self.y = y
        self.imagem = imagem
        self.alcance = 200
        self.dano = dano
        self.cooldown = 400
        self.ultimo_tiro = 0
        self.index_loja = index_loja  # Índice na loja para devolver dinheiro
        
        # Cria a Surface do projétil
        self.projetil_tamanho = 10
        self.imagem_projetil = pygame.Surface((self.projetil_tamanho, self.projetil_tamanho), pygame.SRCALPHA)
        
        cor_projetil = (255, 0, 0) 
        if 'VERMELHO' in globals():
             cor_projetil = VERMELHO
             
        pygame.draw.circle(self.imagem_projetil, cor_projetil, 
                           (self.projetil_tamanho // 2, self.projetil_tamanho // 2), 
                           self.projetil_tamanho // 2)


    def atacar(self, inimigos):
        novos_projeteis = []
        tempo_atual = pygame.time.get_ticks()
        
        if tempo_atual - self.ultimo_tiro < self.cooldown:
            return novos_projeteis

        centro_aliado_x = self.x + 32
        centro_aliado_y = self.y + 32

        inimigo_alvo = None
        for inimigo in inimigos:
            centro_inimigo_x = inimigo.x + inimigo.largura / 2
            centro_inimigo_y = inimigo.y + inimigo.altura / 2

            distancia = math.hypot(centro_inimigo_x - centro_aliado_x,
                                   centro_inimigo_y - centro_aliado_y)

            if distancia <= self.alcance:
                inimigo_alvo = inimigo
                break

        if inimigo_alvo:
            projetil_x = centro_aliado_x
            projetil_y = centro_aliado_y
            
            # Adiciona o novo projétil com o alvo correto
            novos_projeteis.append(Projetil(projetil_x, projetil_y,
                                            centro_inimigo_x, 
                                            centro_inimigo_y,
                                            self.dano, self.imagem_projetil))
            
            self.ultimo_tiro = tempo_atual
            
        return novos_projeteis

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
        