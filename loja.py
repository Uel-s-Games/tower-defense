import pygame

def carregar_loja():
    # Carrega a spritesheet inteira
    sprite_sheet = pygame.image.load('./images/aliados.png').convert_alpha()

    loja = []

    num_personagens = 3
    frame_w = sprite_sheet.get_width() // num_personagens  # largura de cada personagem
    frame_h = sprite_sheet.get_height()                    # altura total é a altura do frame

    # Recorta cada personagem em colunas
    for coluna in range(num_personagens):
        frame = sprite_sheet.subsurface((coluna * frame_w, 0, frame_w, frame_h))
        loja.append(frame)

    return loja
