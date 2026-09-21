from pygame import *

init()
screen = display.set_mode((1280, 720))
running = True
clock = time.Clock()

# --- Carregamento de Recursos ---
fonte = font.Font("Simpsonfont-DEMO.ttf", 65)

homer_img = image.load("homer.png")
homer_img = transform.scale(homer_img, (140, 220))

moita_img = image.load("moita.png")
moita_img = transform.scale(moita_img, (220, 150))

abertura = mixer.Sound("abertura.mp3")

doh_sfx = mixer.Sound("doh.mp3")

pos_nuvem_x = 300  
velocidade_nuvem = 120 
background_color = "#87CEEB" 
texto_titulo = "Simpsons"


# --- Loop Principal do Jogo ---
while running:
    dt = clock.tick(60) / 1000.0

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                background_color = "#F5B240" if background_color == "#87CEEB" else "#87CEEB"
            elif ev.key == K_m:
                doh_sfx.play()

    # --- Funcionamento da Lógica da Nuvem ---
    pos_nuvem_x += velocidade_nuvem * dt
    if pos_nuvem_x > 1280:
        pos_nuvem_x = -250

    
    # --- Desenhos do cenário ---
    
    # Fundo
    screen.fill(background_color)

    # Gramado
    draw.rect(screen, "#38A169", (0, 520, 1280, 200))

    # Sol
    centro_sol = (180, 150)
    draw.circle(screen, "#FFD700", centro_sol, 55)
    
    raios = [
        ((180, 75), (180, 45)),   # Cima
        ((180, 225), (180, 255)), # Baixo
        ((105, 150), (75, 150)),  # Esquerda
        ((255, 150), (285, 150)), # Direita
        ((127, 97), (105, 75)),   # Diag Sup Esq
        ((233, 97), (255, 75)),   # Diag Sup Dir
        ((127, 203), (105, 225)), # Diag Inf Esq
        ((233, 203), (255, 225))  # Diag Inf Dir
    ]
    for inicio, fim in raios:
        draw.line(screen, "#FFD700", inicio, fim, 5)

    # --- Animação da nuvem ---
    y_nuvem = 90
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x), y_nuvem), 45)
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x) + 40, y_nuvem - 15), 50)
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x) + 90, y_nuvem - 10), 45)
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x) + 130, y_nuvem), 40)

    # --- Título Simpsons ---
    texto_surface = fonte.render(texto_titulo, True, "#FFD700")
    sombra_surface = fonte.render(texto_titulo, True, "#000000")
    screen.blit(sombra_surface, (723, 163))
    screen.blit(texto_surface, (720, 160))

    # --- Casa dos Simpsons --- 
    draw.polygon(screen, "#BB5C38", [(250, 480), (550, 480), (400, 280)])
    draw.rect(screen, "#E19B7C", (280, 480, 240, 170))
    draw.rect(screen, "#8B4513", (410, 530, 50, 120))
    draw.circle(screen, "#FFD700", (420, 595), 4)
    draw.rect(screen, "#1A2B56", (310, 530, 60, 60))

    # --- Árvore ---
    draw.rect(screen, "#654321", (980, 420, 60, 230))
    draw.circle(screen, "#2E8B57", (1010, 380), 100)

    # --- Homer e Moita ---
    screen.blit(homer_img, (710, 440))
    screen.blit(moita_img, (670, 510))

    display.update()