# main.py
import pygame
import random
from config import *
from entidades.aliado import Aliado
from entidades.inimigo import Inimigo
from entidades.projetil import Projetil 
from loja import carregar_loja

# Inicializa
pygame.init()
tela = pygame.display.set_mode(TAMANHO_TELA)
pygame.display.set_caption("Tower Defense - Minecraft")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 36)

# Variáveis de jogo
vidas = 10
pontuacao = 0
x_loja = 762

# Fundo
fundo = pygame.image.load('./images/fundo.png')

# Carrega a loja (spritesheet horizontal: Steve, Alex, Esqueleto)
personagens_loja = carregar_loja()

# Controle
aliados = []
inimigos = []
projeteis = [] 
em_arraste = None
tempo_ultima_onda = pygame.time.get_ticks()
intervalo_ondas = 5000  

# Loop principal
rodando = True
while rodando:
    clock.tick(FPS)
    tela.blit(fundo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evento.pos
            if mx > x_loja:
                index = (my // 150) % len(personagens_loja)
                em_arraste = personagens_loja[index]
            else:
                for aliado in aliados:
                    if aliado.x < mx < aliado.x + 64 and aliado.y < my < aliado.y + 64:
                        em_arraste = aliado
                        aliados.remove(aliado)
                        break

        elif evento.type == pygame.MOUSEBUTTONUP:
            if em_arraste:
                mx, my = evento.pos
                if mx < x_loja:
                    if isinstance(em_arraste, pygame.Surface):
                        aliados.append(Aliado(mx - 32, my - 32, em_arraste))
                    else:
                        em_arraste.x = mx - 32
                        em_arraste.y = my - 32
                        aliados.append(em_arraste)
                em_arraste = None

    # Ondas de inimigos
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_ultima_onda > intervalo_ondas:
        for i in range(5):
            inimigos.append(Inimigo(CAMINHO_INIMIGOS))
        tempo_ultima_onda = tempo_atual

    # Aliados atacam (geram projéteis)
    novos_projeteis_gerados = []
    for aliado in aliados:
        novos_projeteis_gerados.extend(aliado.atacar(inimigos))
    projeteis.extend(novos_projeteis_gerados) 

    # Projéteis se movem e verificam colisão
    for projetil in projeteis[:]: 
        saiu_da_tela = projetil.mover()
        if saiu_da_tela:
            projeteis.remove(projetil)
            continue
            
        for inimigo in inimigos[:]: 
            if projetil.rect.colliderect(inimigo.rect) and not projetil.atingiu:
                inimigo.vida = max(inimigo.vida - projetil.dano, 0)
                projetil.atingiu = True
                projeteis.remove(projetil)
                break
        else:
            projetil.desenhar(tela)
    
    # Inimigos se movem, morrem e são desenhados
    for inimigo in inimigos[:]:
        chegou = inimigo.mover()
        if chegou:
            vidas -= 1
            inimigos.remove(inimigo)
        elif inimigo.vida <= 0:
            pontuacao += 10
            inimigos.remove(inimigo)
        else:
            inimigo.desenhar(tela)

    # Desenho dos aliados
    for aliado in aliados:
        aliado.desenhar(tela)

    # Loja e HUD
    pygame.draw.rect(tela, (180,180,180), (x_loja, 0, 1024 - x_loja, 768))
    for i, img in enumerate(personagens_loja):
        tela.blit(img, (x_loja + 10, 50 + i * 150))

    texto = fonte.render(f"Vidas: {vidas}  Pontos: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto, (20, 20))

    # Arraste
    if em_arraste:
        mx, my = pygame.mouse.get_pos()
        if isinstance(em_arraste, pygame.Surface):
            tela.blit(em_arraste, (mx - 32, my - 32))
        else:
            tela.blit(em_arraste.imagem, (mx - 32, my - 32))

    # Game Over
    if vidas <= 0:
        texto = fonte.render("GAME OVER!", True, (255, 0, 0))
        tela.blit(texto, (400, 350))
        pygame.display.update()
        pygame.time.delay(3000)
        rodando = False

    pygame.display.update()

pygame.quit()
