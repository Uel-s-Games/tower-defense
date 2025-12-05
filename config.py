# config.py
import pygame

pygame.init()

# TELA
TAMANHO_TELA = (1024, 768)
FPS = 60

# CORES
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 200, 0)
VERMELHO = (255, 0, 0)
CINZA = (50, 50, 50)
AMARELO = (255, 255, 0)  # <-- adicionei esta linha
AZUL = (100, 150, 255)

# OUTROS
DINHEIRO_INICIAL = 200  # Apenas para comprar 2 Steves no início
CUSTOS_ALIADOS = [100, 500, 800]  # Custos para cada tipo de aliado
DANOS_ALIADOS = [12, 20, 30]  # Danos para cada tipo de aliado (Steve, Alex, Esqueleto) - reduzido
RECOMPENSA_INIMIGO = 9  # Dinheiro ganho ao matar inimigo (reduzido ainda mais para dificultar)
MAX_ALIADOS = 14  # Limite máximo de aliados no mapa

CAMINHO_INIMIGOS = [
    (18, 607),
    (172, 607),
    (295, 591),
    (289, 439),
    (393, 438),
    (398, 584),
    (395, 688),
    (482, 753),
    (636, 745),
    (687, 724),
    (677, 474),
    (681, 129)
]

# FASES DO JOGO
FASES = [
    {
        'nome': 'Fase 1',
        'ondas': 8,
        'inimigos_base_onda': 4,  # Número base que aumenta a cada onda
        'aumento_por_onda': 1,  # Aumenta 1 inimigo por onda
        'intervalo_ondas': 8000,
        'tem_boss': False
    },
    {
        'nome': 'Fase 2',
        'ondas': 10,
        'inimigos_base_onda': 6,
        'aumento_por_onda': 1,
        'intervalo_ondas': 7500,
        'tem_boss': False
    },
    {
        'nome': 'Fase 3',
        'ondas': 12,
        'inimigos_base_onda': 8,
        'aumento_por_onda': 2,
        'intervalo_ondas': 7000,
        'tem_boss': True,
        'boss_vida': 2500,
        'boss_velocidade': 1.5,
        'boss_tamanho': 48
    },
    {
        'nome': 'Fase 4',
        'ondas': 15,
        'inimigos_base_onda': 10,
        'aumento_por_onda': 2,
        'intervalo_ondas': 6500,
        'tem_boss': False
    },
    {
        'nome': 'Fase 5',
        'ondas': 18,
        'inimigos_base_onda': 12,
        'aumento_por_onda': 3,
        'intervalo_ondas': 6000,
        'tem_boss': True,
        'boss_vida': 4500,
        'boss_velocidade': 1.8,
        'boss_tamanho': 56
    }
]

RECOMPENSA_BOSS = 80  # Dinheiro ganho ao matar boss (reduzido ainda mais)
