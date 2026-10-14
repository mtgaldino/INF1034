from pygame import *
import os

init()
screen = display.set_mode((1280, 720))
display.set_caption("La Casita ULTIMATE - Simpsons")
running = True
clock = time.Clock()

PASTA_BASE = os.path.dirname(__file__)


fonte = font.Font(os.path.join(PASTA_BASE, "Simpsonfont-DEMO.otf"), 65)

homer_img = image.load(os.path.join(PASTA_BASE, "homer.png"))
homer_img = transform.scale(homer_img, (140, 220))

moita_img = image.load(os.path.join(PASTA_BASE, "moita.png"))
moita_img = transform.scale(moita_img, (220, 150))


mixer.music.load(os.path.join(PASTA_BASE, "audio-simpsons.mp3"))
mixer.music.set_volume(0.3)
mixer.music.play(loops=-1)

sfx_manha = mixer.Sound(os.path.join(PASTA_BASE, "doh.wav"))
sfx_tarde = mixer.Sound(os.path.join(PASTA_BASE, "doh.wav"))
sfx_noite = mixer.Sound(os.path.join(PASTA_BASE, "doh.wav"))


pos_nuvem_x = 300.0
velocidade_nuvem = 150.0

pos_sol_x = 180.0
pos_sol_y = 150.0
velocidade_sol = 300.0
raio_sol = 50

texto_titulo = "Simpsons"


COR_MANHA = (135, 206, 235)  
COR_TARDE = (245, 178, 64)   
COR_NOITE = (25, 25, 112)    

def interpolar_cor(cor1, cor2, t):
    r = int(cor1[0] + (cor2[0] - cor1[0]) * t)
    g = int(cor1[1] + (cor2[1] - cor1[1]) * t)
    b = int(cor1[2] + (cor2[2] - cor1[2]) * t)
    return (r, g, b)


while running:
    dt = clock.tick(60) / 1000.0
    
    
    for ev in event.get():
        if ev.type == QUIT:
            running = False
            
        elif ev.type == MOUSEBUTTONDOWN:
            
            if pos_sol_x < 426:
                sfx_manha.play()
            elif pos_sol_x < 852:
                sfx_tarde.play()
            else:
                sfx_noite.play()

    
    teclas = key.get_pressed()
    
    
    if teclas[K_LEFT] or teclas[K_a]:
        pos_sol_x -= velocidade_sol * dt
    if teclas[K_RIGHT] or teclas[K_d]:
        pos_sol_x += velocidade_sol * dt
    if teclas[K_UP] or teclas[K_w]:
        pos_sol_y -= velocidade_sol * dt
    if teclas[K_DOWN] or teclas[K_s]:
        pos_sol_y += velocidade_sol * dt

    
    mouse_x, mouse_y = mouse.get_pos()
    botoes_mouse = mouse.get_pressed()
    if botoes_mouse[0]:  
        pos_sol_x, pos_sol_y = mouse_x, mouse_y

    
    pos_sol_x = max(raio_sol + 30, min(pos_sol_x, 1280 - (raio_sol + 30)))
    pos_sol_y = max(raio_sol + 30, min(pos_sol_y, 520 - (raio_sol + 30)))

    
    fator_dia = pos_sol_x / 1280.0
    
    if fator_dia < 0.5:
        
        t = fator_dia / 0.5
        cor_fundo = interpolar_cor(COR_MANHA, COR_TARDE, t)
    else:
        
        t = (fator_dia - 0.5) / 0.5
        cor_fundo = interpolar_cor(COR_TARDE, COR_NOITE, t)

    
    pos_nuvem_x += velocidade_nuvem * dt
    if pos_nuvem_x > 1280 - 200:  
        pos_nuvem_x = 1280 - 200
        velocidade_nuvem = -velocidade_nuvem
    elif pos_nuvem_x < 0:         
        pos_nuvem_x = 0
        velocidade_nuvem = -velocidade_nuvem
    
    screen.fill(cor_fundo)
    
    draw.rect(screen, "#38A169", (0, 520, 1280, 200))
    
    cx, cy = int(pos_sol_x), int(pos_sol_y)
    draw.circle(screen, "#FFD700", (cx, cy), raio_sol)
    
    tam_raio_min = raio_sol + 10
    tam_raio_max = raio_sol + 30
    
    
    offsets_raios = [
        (0, -1), (0, 1), (-1, 0), (1, 0),          
        (-0.7, -0.7), (0.7, -0.7), (-0.7, 0.7), (0.7, 0.7) 
    ]
    for dx, dy in offsets_raios:
        p_inicio = (int(cx + dx * tam_raio_min), int(cy + dy * tam_raio_min))
        p_fim = (int(cx + dx * tam_raio_max), int(cy + dy * tam_raio_max))
        draw.line(screen, "#FFD700", p_inicio, p_fim, 4)

    
    y_nuvem = 90
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x) + 40, y_nuvem), 40)
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x) + 80, y_nuvem - 15), 45)
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x) + 120, y_nuvem - 10), 40)
    draw.circle(screen, "#FFFFFF", (int(pos_nuvem_x) + 150, y_nuvem), 35)

    
    texto_surface = fonte.render(texto_titulo, True, "#FFD700")
    sombra_surface = fonte.render(texto_titulo, True, "#000000")
    screen.blit(sombra_surface, (723, 163))
    screen.blit(texto_surface, (720, 160))

    draw.polygon(screen, "#BB5C38", [(250, 480), (550, 480), (400, 280)])
    draw.rect(screen, "#E19B7C", (280, 480, 240, 170))
    draw.rect(screen, "#8B4513", (410, 530, 50, 120))
    draw.circle(screen, "#FFD700", (420, 595), 4)
    draw.rect(screen, "#1A2B56", (310, 530, 60, 60))

    draw.rect(screen, "#654321", (980, 420, 60, 230))
    draw.circle(screen, "#2E8B57", (1010, 380), 100)

    screen.blit(homer_img, (710, 440))
    screen.blit(moita_img, (670, 510))

    display.update()

quit()