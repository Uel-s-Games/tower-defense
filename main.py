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
fonte_titulo = pygame.font.SysFont(None, 72)
fonte_pequena = pygame.font.SysFont(None, 24)

# Fundo
fundo = pygame.image.load('./images/fundo.png')

# Carrega a loja (spritesheet horizontal: Steve, Alex, Esqueleto)
personagens_loja = carregar_loja()

# Estados do jogo
ESTADO_MENU = 0
ESTADO_JOGANDO = 1
ESTADO_PAUSADO = 2
ESTADO_GAME_OVER = 3
ESTADO_VITORIA = 4
estado_atual = ESTADO_MENU

# Função para desenhar botão
def desenhar_botao(tela, texto, x, y, largura, altura, cor_normal, cor_hover, mouse_pos):
    mouse_x, mouse_y = mouse_pos
    hover = (x <= mouse_x <= x + largura and y <= mouse_y <= y + altura)
    cor = cor_hover if hover else cor_normal
    
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    pygame.draw.rect(tela, BRANCO, (x, y, largura, altura), 3)
    
    texto_renderizado = fonte.render(texto, True, BRANCO)
    texto_rect = texto_renderizado.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_renderizado, texto_rect)
    
    return hover

# Função para o menu inicial
def mostrar_menu_inicial():
    global estado_atual, rodando
    
    while estado_atual == ESTADO_MENU and rodando:
        clock.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Botão "Jogar"
                if 350 <= mx <= 650 and 350 <= my <= 420:
                    estado_atual = ESTADO_JOGANDO
                    return
                # Botão "Sair"
                elif 350 <= mx <= 650 and 450 <= my <= 520:
                    rodando = False
                    return
        
        # Fundo
        tela.blit(fundo, (0, 0))
        
        # Título
        titulo = fonte_titulo.render("TOWER DEFENSE", True, BRANCO)
        titulo_rect = titulo.get_rect(center=(TAMANHO_TELA[0] // 2, 150))
        tela.blit(titulo, titulo_rect)
        
        subtitulo = fonte.render("MINECRAFT EDITION", True, VERDE)
        subtitulo_rect = subtitulo.get_rect(center=(TAMANHO_TELA[0] // 2, 220))
        tela.blit(subtitulo, subtitulo_rect)
        
        # Botões
        mx, my = pygame.mouse.get_pos()
        desenhar_botao(tela, "JOGAR", 350, 350, 300, 70, (50, 150, 50), (0, 200, 0), (mx, my))
        desenhar_botao(tela, "SAIR", 350, 450, 300, 70, (150, 50, 50), (200, 0, 0), (mx, my))
        
        pygame.display.update()

# Função para o menu de pausa
def mostrar_menu_pausa():
    global estado_atual, rodando
    
    while estado_atual == ESTADO_PAUSADO and rodando:
        clock.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    estado_atual = ESTADO_JOGANDO
                    return
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Botão "Continuar"
                if 350 <= mx <= 650 and 300 <= my <= 370:
                    estado_atual = ESTADO_JOGANDO
                    return
                # Botão "Menu Principal"
                elif 350 <= mx <= 650 and 400 <= my <= 470:
                    estado_atual = ESTADO_MENU
                    return
                # Botão "Sair"
                elif 350 <= mx <= 650 and 500 <= my <= 570:
                    rodando = False
                    return
        
        # Desenha uma sobreposição semitransparente
        overlay = pygame.Surface(TAMANHO_TELA)
        overlay.set_alpha(180)
        overlay.fill(PRETO)
        tela.blit(overlay, (0, 0))
        
        # Título
        pausado = fonte_titulo.render("PAUSADO", True, BRANCO)
        pausado_rect = pausado.get_rect(center=(TAMANHO_TELA[0] // 2, 200))
        tela.blit(pausado, pausado_rect)
        
        # Botões
        mx, my = pygame.mouse.get_pos()
        desenhar_botao(tela, "CONTINUAR", 350, 300, 300, 70, (50, 150, 50), (0, 200, 0), (mx, my))
        desenhar_botao(tela, "MENU PRINCIPAL", 350, 400, 300, 70, (100, 100, 150), (120, 120, 200), (mx, my))
        desenhar_botao(tela, "SAIR", 350, 500, 300, 70, (150, 50, 50), (200, 0, 0), (mx, my))
        
        pygame.display.update()

# Função para a tela de vitória
def mostrar_tela_vitoria():
    global estado_atual, rodando
    
    while estado_atual == ESTADO_VITORIA and rodando:
        clock.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Botão "Menu Principal"
                if 350 <= mx <= 650 and 350 <= my <= 420:
                    estado_atual = ESTADO_MENU
                    return
                # Botão "Sair"
                elif 350 <= mx <= 650 and 450 <= my <= 520:
                    rodando = False
                    return
        
        # Fundo
        tela.blit(fundo, (0, 0))
        
        # Overlay
        overlay = pygame.Surface(TAMANHO_TELA)
        overlay.set_alpha(150)
        overlay.fill(PRETO)
        tela.blit(overlay, (0, 0))
        
        # Título
        titulo = fonte_titulo.render("PARABÉNS!", True, VERDE)
        titulo_rect = titulo.get_rect(center=(TAMANHO_TELA[0] // 2, 200))
        tela.blit(titulo, titulo_rect)
        
        subtitulo = fonte.render("BOM JOGO!", True, AMARELO)
        subtitulo_rect = subtitulo.get_rect(center=(TAMANHO_TELA[0] // 2, 280))
        tela.blit(subtitulo, subtitulo_rect)
        
        # Botões
        mx, my = pygame.mouse.get_pos()
        desenhar_botao(tela, "MENU PRINCIPAL", 350, 350, 300, 70, (50, 150, 50), (0, 200, 0), (mx, my))
        desenhar_botao(tela, "SAIR", 350, 450, 300, 70, (150, 50, 50), (200, 0, 0), (mx, my))
        
        pygame.display.update()

# Loop principal
rodando = True
while rodando:
    # Mostra menu inicial
    if estado_atual == ESTADO_MENU:
        mostrar_menu_inicial()
        if not rodando:
            break
        
        # Inicializa variáveis de jogo para novo jogo
        vidas = 10
        dinheiro = DINHEIRO_INICIAL
        x_loja = 762
        
        # Sistema de fases
        fase_atual = 0
        onda_atual = 0
        mostrar_fase = False
        tempo_mostrar_fase = 0
        boss_spawnado_na_fase = False  # Controla se o boss já foi spawnado na fase atual
        
        # Sistema de spawn com delay
        fila_spawn = []  # Lista de inimigos a serem spawnados: [(tempo_spawn, offset_x, offset_y), ...]
        tempo_ultimo_spawn = 0
        
        # Controle
        aliados = []
        inimigos = []
        projeteis = []
        em_arraste = None
        tempo_ultima_onda = pygame.time.get_ticks()
        intervalo_ondas = 8000
    
    # Loop do jogo
    clock.tick(FPS)
    
    # Desenha o fundo PRIMEIRO (exceto quando está no menu ou pausado)
    if estado_atual == ESTADO_JOGANDO:
        tela.blit(fundo, (0, 0))
    
    if estado_atual == ESTADO_JOGANDO:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    estado_atual = ESTADO_PAUSADO

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = evento.pos
                if mx > x_loja:
                    # Ajusta para o y_pos = 100
                    y_ajustado = my - 100
                    if y_ajustado >= 0:
                        index = (y_ajustado // 150) % len(personagens_loja)
                        if 0 <= index < len(CUSTOS_ALIADOS):
                            custo = CUSTOS_ALIADOS[index]
                            # Verifica se tem dinheiro suficiente E se não atingiu o limite
                            if dinheiro >= custo and len(aliados) < MAX_ALIADOS:
                                em_arraste = (personagens_loja[index], index)
                else:
                    # Botão direito para vender, botão esquerdo para mover
                    if evento.button == 3:  # Botão direito
                        # Vender aliado
                        for aliado in aliados:
                            if aliado.x < mx < aliado.x + 64 and aliado.y < my < aliado.y + 64:
                                # Devolve metade do dinheiro (preço de venda)
                                for idx, img in enumerate(personagens_loja):
                                    if img == aliado.imagem:
                                        dinheiro_devolvido = CUSTOS_ALIADOS[idx] // 2  # 50% do valor
                                        dinheiro += dinheiro_devolvido
                                        break
                                aliados.remove(aliado)
                                break
                    elif evento.button == 1:  # Botão esquerdo
                        # Mover aliado
                        for aliado in aliados:
                            if aliado.x < mx < aliado.x + 64 and aliado.y < my < aliado.y + 64:
                                em_arraste = aliado
                                aliados.remove(aliado)
                                break

            elif evento.type == pygame.MOUSEBUTTONUP:
                if em_arraste:
                    mx, my = evento.pos
                    if mx < x_loja:
                        if isinstance(em_arraste, tuple):
                            # Compra de loja
                            imagem, index = em_arraste
                            custo = CUSTOS_ALIADOS[index]
                            dano = DANOS_ALIADOS[index]
                            # Verifica limite novamente antes de comprar
                            if len(aliados) < MAX_ALIADOS:
                                dinheiro -= custo
                                aliados.append(Aliado(mx - 32, my - 32, imagem, dano=dano, index_loja=index))
                            else:
                                # Limite atingido, não compra (o item volta para a loja automaticamente)
                                pass
                        else:
                            # Se arrastou para a loja, devolve o dinheiro
                            if mx >= x_loja:
                                # Devolve todo o dinheiro gasto
                                dinheiro += CUSTOS_ALIADOS[em_arraste.index_loja]
                                # Não adiciona o aliado de volta (foi devolvido)
                            else:
                                # Reposicionar aliado existente (não cobra dinheiro novamente)
                                em_arraste.x = mx - 32
                                em_arraste.y = my - 32
                                aliados.append(em_arraste)
                    em_arraste = None

        # Sistema de fases e ondas
        tempo_atual = pygame.time.get_ticks()
        
        # Verifica se acabaram todas as ondas e inimigos da fase atual
        if fase_atual < len(FASES):
            fase = FASES[fase_atual]
            
            # Envia ondas baseado no intervalo de tempo
            if onda_atual < fase['ondas']:
                # Se já passou o intervalo de ondas
                if tempo_atual - tempo_ultima_onda > fase['intervalo_ondas']:
                    # Calcula número de inimigos para esta onda (aumenta progressivamente)
                    inimigos_esta_onda = fase['inimigos_base_onda'] + (onda_atual * fase['aumento_por_onda'])
                    
                    # Adiciona inimigos na fila de spawn com delay e espaçamento
                    delay_entre_inimigos = 400  # 400ms entre cada inimigo
                    offset_espacamento = 35  # Espaçamento em pixels
                    
                    for i in range(inimigos_esta_onda):
                        tempo_spawn = tempo_atual + (i * delay_entre_inimigos)
                        # Espaçamento em linha: inimigos aparecem em uma linha com pequeno espaçamento
                        # Cada inimigo fica um pouco atrás do anterior
                        offset_x = -i * offset_espacamento  # Deslocamento horizontal (para trás)
                        offset_y = (i % 2) * 15 - 7  # Pequeno deslocamento vertical alternado
                        fila_spawn.append((tempo_spawn, offset_x, offset_y))
                    
                    onda_atual += 1
                    tempo_ultima_onda = tempo_atual
            
            # Processa a fila de spawn
            for spawn_info in fila_spawn[:]:
                tempo_spawn, offset_x, offset_y = spawn_info
                if tempo_atual >= tempo_spawn:
                    # Cria o inimigo com offset na posição inicial
                    inimigo = Inimigo(CAMINHO_INIMIGOS)
                    inimigo.x += offset_x
                    inimigo.y += offset_y
                    inimigo.rect.topleft = (int(inimigo.x), int(inimigo.y))
                    inimigos.append(inimigo)
                    fila_spawn.remove(spawn_info)
            
            # Verifica se é a última onda e tem boss
            if onda_atual >= fase['ondas'] and fase.get('tem_boss', False) and not boss_spawnado_na_fase:
                # Verifica se já existe um boss na tela
                boss_spawnado = False
                for inimigo in inimigos:
                    if hasattr(inimigo, 'is_boss'):
                        boss_spawnado = True
                        break
                
                # Spawna o boss após um intervalo sem inimigos na tela
                if not boss_spawnado and len(inimigos) == 0 and tempo_atual - tempo_ultima_onda > fase['intervalo_ondas']:
                    boss = Inimigo(
                        CAMINHO_INIMIGOS,
                        vida=fase['boss_vida'],
                        velocidade=fase['boss_velocidade'],
                        tamanho=fase['boss_tamanho'],
                        cor=(200, 0, 0)  # Vermelho escuro para boss
                    )
                    boss.is_boss = True
                    inimigos.append(boss)
                    boss_spawnado_na_fase = True
                    
            # Avança para próxima fase se acabaram os inimigos E já derrotou o boss (se houver)
            if len(inimigos) == 0 and onda_atual >= fase['ondas']:
                # Se tinha boss, verifica se foi derrotado (não avança ainda se o boss ainda não spawnou)
                if fase.get('tem_boss', False):
                    # Verifica se já spawnou o boss e foi derrotado
                    boss_existe_ou_spawnou = any(hasattr(inimigo, 'is_boss') for inimigo in inimigos)
                    if not boss_existe_ou_spawnou:
                        # Boss ainda não foi spawnado ou já foi derrotado
                        if fase_atual < len(FASES) - 1:
                            # Avança de fase
                            fase_atual += 1
                            onda_atual = 0
                            mostrar_fase = True
                            tempo_mostrar_fase = tempo_atual
                            tempo_ultima_onda = tempo_atual
                            boss_spawnado_na_fase = False  # Reseta para próxima fase
                            fila_spawn = []  # Limpa a fila de spawn
                        elif fase_atual == len(FASES) - 1:
                            # Última fase: vitória!
                            if len(inimigos) == 0 and len(fila_spawn) == 0:
                                estado_atual = ESTADO_VITORIA
                else:
                    # Não tem boss, avança de fase normalmente
                    if fase_atual < len(FASES) - 1:
                        fase_atual += 1
                        onda_atual = 0
                        mostrar_fase = True
                        tempo_mostrar_fase = tempo_atual
                        tempo_ultima_onda = tempo_atual
                        boss_spawnado_na_fase = False  # Reseta para próxima fase
                        fila_spawn = []  # Limpa a fila de spawn
                    # Se é a última fase e acabaram todos os inimigos, venceu
                    elif fase_atual == len(FASES) - 1:
                        # Verifica se não há mais inimigos e não há boss
                        if len(inimigos) == 0 and len(fila_spawn) == 0:
                            estado_atual = ESTADO_VITORIA

        # Inimigos se movem PRIMEIRO
        for inimigo in inimigos[:]:
            chegou = inimigo.mover()
            if chegou:
                vidas -= 1
                inimigos.remove(inimigo)
            elif inimigo.vida <= 0:
                # Dá mais recompensa se for boss
                if hasattr(inimigo, 'is_boss') and inimigo.is_boss:
                    dinheiro += RECOMPENSA_BOSS
                else:
                    dinheiro += RECOMPENSA_INIMIGO
                inimigos.remove(inimigo)
        
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

        # Inimigos são desenhados
        for inimigo in inimigos:
            inimigo.desenhar(tela)

        # Desenho dos aliados
        for aliado in aliados:
            aliado.desenhar(tela)

        # Loja e HUD
        pygame.draw.rect(tela, (180, 180, 180), (x_loja, 0, 1024 - x_loja, 768))
        
        # Desenha a loja com verificação de dinheiro
        for i, img in enumerate(personagens_loja):
            y_pos = 100 + i * 150
            custo = CUSTOS_ALIADOS[i]
            
            # Verifica se tem dinheiro suficiente e se não atingiu o limite
            tem_dinheiro = dinheiro >= custo
            pode_comprar = len(aliados) < MAX_ALIADOS
            pode_comprar_item = tem_dinheiro and pode_comprar
            
            # Se não tem dinheiro ou atingiu limite, desenha em tons de cinza
            if not pode_comprar_item:
                img_cinza = img.copy()
                # Aplica um overlay cinza usando blend
                img_cinza.fill((100, 100, 100, 255), special_flags=pygame.BLEND_RGBA_MULT)
                tela.blit(img_cinza, (x_loja + 10, y_pos))
            else:
                tela.blit(img, (x_loja + 10, y_pos))
            
            # Desenha o preço
            cor_preco = PRETO if pode_comprar_item else (100, 100, 100)
            texto_preco = fonte_pequena.render(f"{custo} coins", True, cor_preco)
            tela.blit(texto_preco, (x_loja + 10, y_pos + 70))
            
            # Mostra mensagem se atingiu limite
            if not pode_comprar and len(aliados) >= MAX_ALIADOS:
                texto_limite = fonte_pequena.render("LIMITE!", True, VERMELHO)
                tela.blit(texto_limite, (x_loja + 10, y_pos + 85))

        # HUD
        texto = fonte.render(f"Vidas: {vidas}", True, (255, 255, 255))
        tela.blit(texto, (20, 20))
        
        texto_dinheiro = fonte.render(f"Coins: {dinheiro}", True, AMARELO)
        tela.blit(texto_dinheiro, (20, 60))
        
        # Mostra limite de aliados
        texto_aliados = fonte_pequena.render(f"Aliados: {len(aliados)}/{MAX_ALIADOS}", True, (255, 255, 255))
        tela.blit(texto_aliados, (20, 100))
        
        # Mostra a fase atual
        if fase_atual < len(FASES):
            texto_fase = fonte.render(f"{FASES[fase_atual]['nome']} - Onda {onda_atual}/{FASES[fase_atual]['ondas']}", True, (255, 255, 255))
            tela.blit(texto_fase, (20, 130))
        
        # Mostra mensagem ao mudar de fase
        if mostrar_fase and fase_atual > 0:
            tempo_agora = pygame.time.get_ticks()
            if tempo_agora - tempo_mostrar_fase < 3000:  # Mostra por 3 segundos
                overlay = pygame.Surface(TAMANHO_TELA)
                overlay.set_alpha(180)
                overlay.fill(PRETO)
                tela.blit(overlay, (0, 0))
                
                msg_fase = fonte_titulo.render(FASES[fase_atual-1]['nome'] + " COMPLETA!", True, VERDE)
                msg_rect = msg_fase.get_rect(center=(TAMANHO_TELA[0] // 2, TAMANHO_TELA[1] // 2))
                tela.blit(msg_fase, msg_rect)
            else:
                mostrar_fase = False

        # Arraste
        if em_arraste:
            mx, my = pygame.mouse.get_pos()
            if isinstance(em_arraste, tuple):
                imagem, index = em_arraste
                custo = CUSTOS_ALIADOS[index]
                # Se não tiver dinheiro suficiente, não permite arrastar
                if dinheiro >= custo:
                    tela.blit(imagem, (mx - 32, my - 32))
            else:
                tela.blit(em_arraste.imagem, (mx - 32, my - 32))

        # Game Over
        if vidas <= 0:
            estado_atual = ESTADO_GAME_OVER
            texto = fonte_titulo.render("GAME OVER!", True, VERMELHO)
            tela.blit(texto, (400, 350))
            pygame.display.update()
            pygame.time.delay(3000)
            estado_atual = ESTADO_MENU

    # Mostra menu de pausa
    if estado_atual == ESTADO_PAUSADO:
        mostrar_menu_pausa()
        if not rodando:
            break
    
    # Mostra tela de vitória
    if estado_atual == ESTADO_VITORIA:
        mostrar_tela_vitoria()
        if not rodando:
            break
    
    pygame.display.update()

pygame.quit()
