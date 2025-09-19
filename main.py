import pygame


# Inicializa
pygame.init()

# Funções do jogo
tamanho_tela = (1024,768)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Tower Defense - Minecraft")

steve_img = pygame.image.load('./images/steve.png')
steve_x = 100
steve_y = 100

clock = pygame.time.Clock()

# Loop infinito
rodando = True
while rodando:
    
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill((0,0,0))

    tela.blit(steve_img, (steve_x, steve_y))
    pygame.display.update()
    

pygame.quit()