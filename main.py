import pygame

# Inicializa
pygame.init()

# Funções do jogo
tamanho_tela = (1024,768)

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Tower Defense - Minecraft")

steve_x = 100
steve_y = 100

fundo = pygame.image.load('./images/fundo.png')


 
x_loja = 762
largura = 1022 - x_loja
y_loja = 764
tamanho_loja = (x_loja, y_loja)

personagens_loja = pygame.image.load('./images/aliados.png')
frame_w = 128
frame_h = 128

def get_frames_loja(linha):
    frames = []
    for i in range(3):
        frame = sprite_steve.subsurface((i * frame_w, linha * frame_h, frame_w, frame_h))
        frames.append(frame)
    return frames


sprite_steve = pygame.image.load('./images/sprites_steve.png')
frame_w = 64
frame_h = 64

def get_frames_steve(linha):
    frames = []
    for i in range(3):
        frame = sprite_steve.subsurface((i * frame_w, linha * frame_h, frame_w, frame_h))
        frames.append(frame)
    return frames

# Direções do steve
direita = get_frames_steve(0)
esquerda = get_frames_steve(1)
cima_esquerda = get_frames_steve(2)
cima_direita = get_frames_steve(3)
baixo_direita = get_frames_steve(4)
baixo_esquerda = get_frames_steve(5)


clock = pygame.time.Clock()

# Loop infinito
rodando = True
while rodando:
    
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    if evento.type == pygame.MOUSEBUTTONDOWN:
        print(evento.pos)


    # Tela de fundo e steve
    tela.blit(fundo, (0,0))
    pygame.display.update()
    

pygame.quit()