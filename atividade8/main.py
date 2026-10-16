import os
import subprocess
import sys
 
import pygame
 
from validar_login import (valida_email, valida_senha, criptografa_senha, descriptografa_senha)

PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
 
LARGURA = 800
ALTURA = 600

FUNDO = (235, 240, 250)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (190, 190, 190)
AZUL = (30, 90, 200)
AZUL_CLARO = (90, 140, 230)
VERMELHO = (200, 30, 30)
VERDE = (20, 140, 60)

PROJETOS = [
    ("1 - Casinha (Simpsons)", "casa_simpsons.py"),
    ("2 - Jogo de Adivinhação", "adivinhacao.py"),
    ("3 - Pedra, Papel e Tesoura", "pedra_papel_tesoura.py"),
]
 
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Login - Projetos Pygame")
relogio = pygame.time.Clock()
 
fonte_titulo = pygame.font.Font(None, 64)
fonte = pygame.font.Font(None, 36)
fonte_pequena = pygame.font.Font(None, 26)

def escrever(texto, fonte_usada, cor, posicao, centralizar=False):
    if texto == "":
        return
    imagem = fonte_usada.render(texto, True, cor)
    if centralizar:
        retangulo = imagem.get_rect(center=posicao)
    else:
        retangulo = imagem.get_rect(topleft=posicao)
    tela.blit(imagem, retangulo)
    
def desenhar_botao(retangulo, texto):
    if retangulo.collidepoint(pygame.mouse.get_pos()):
        cor = AZUL_CLARO
    else:
        cor = AZUL
    pygame.draw.rect(tela, cor, retangulo, border_radius=8)
    escrever(texto, fonte, BRANCO, retangulo.center, True)
    
def verificar_login(email, senha):
    if not valida_email(email):
        return "E-mail inválido: precisa terminar com @puc.com"
    if not valida_senha(senha):
        return "Senha fraca: use 8+ caracteres, com maiúscula, minúscula e número"
    return ""

def tela_login():
    textos = ["", ""]
    campo = 0
    mensagem = ""
    caixas = [pygame.Rect(150, 180, 500, 45), pygame.Rect(150, 280, 500, 45)]
    nomes = ["E-mail:", "Senha:"]
    botao = pygame.Rect(300, 370, 200, 50)
    
    while True:
        relogio.tick(30)
        entrar = False
 
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return None
 
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if caixas[0].collidepoint(ev.pos):
                    campo = 0
                elif caixas[1].collidepoint(ev.pos):
                    campo = 1
                elif botao.collidepoint(ev.pos):
                    entrar = True
            
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_TAB:
                    campo = 1 - campo
                elif ev.key == pygame.K_BACKSPACE:
                    textos[campo] = textos[campo][:-1]
                elif ev.key == pygame.K_RETURN:
                    entrar = True
                elif ev.unicode != "" and ev.unicode.isprintable() and len(textos[campo]) < 30:
                    textos[campo] += ev.unicode
                    
        if entrar:
            mensagem = verificar_login(textos[0], textos[1])
            if mensagem == "":
                return textos[0], textos[1]
        
        tela.fill(FUNDO)
        escrever("Login", fonte_titulo, AZUL, (LARGURA // 2, 80), True)
        
        for i in range(2):
            escrever(nomes[i], fonte, PRETO, (150, caixas[i].y - 32))
            pygame.draw.rect(tela, BRANCO, caixas[i])
            if i == campo:
                cor_borda = AZUL
            else:
                cor_borda = CINZA
            pygame.draw.rect(tela, cor_borda, caixas[i], 3)
 
            if i == 0:
                texto_mostrado = textos[i]
            else:
                texto_mostrado = "*" * len(textos[i])
            escrever(texto_mostrado, fonte, PRETO, (caixas[i].x + 10, caixas[i].y + 10))
 
        desenhar_botao(botao, "Entrar")
        escrever(mensagem, fonte_pequena, VERMELHO, (LARGURA // 2, 450), True)
        escrever("TAB troca de campo  |  ENTER confirma", fonte_pequena, CINZA, (LARGURA // 2, 550), True)
        pygame.display.update()
        
def tela_senha(senha):
    cripto = criptografa_senha(senha)
    decripto = descriptografa_senha(cripto)
    
    while True:
        relogio.tick(30)
 
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return True
 
        tela.fill(FUNDO)
        escrever("Login realizado!", fonte_titulo, VERDE, (LARGURA // 2, 90), True)
        escrever("Senha criptografada:", fonte, PRETO, (LARGURA // 2, 210), True)
        escrever(cripto, fonte_titulo, AZUL, (LARGURA // 2, 260), True)
        escrever("Senha descriptografada:", fonte, PRETO, (LARGURA // 2, 350), True)
        escrever(decripto, fonte_titulo, AZUL, (LARGURA // 2, 400), True)
        escrever("Pressione ENTER para continuar", fonte_pequena, CINZA, (LARGURA // 2, 540), True)
        pygame.display.update()
        
def abrir_projeto(arquivo):
    caminho = os.path.join(PASTA_BASE, arquivo)
    resultado = subprocess.run([sys.executable, caminho], cwd=PASTA_BASE)
    return resultado.returncode == 0

def desenhar_menu(botoes, aviso, cor_aviso):
    tela.fill(FUNDO)
    escrever("Menu de Projetos", fonte_titulo, AZUL, (LARGURA // 2, 80), True)
    escrever("Clique ou aperte 1, 2 ou 3  (ESC para sair)", fonte_pequena, CINZA, (LARGURA // 2, 130), True)
    for i in range(len(botoes)):
        desenhar_botao(botoes[i], PROJETOS[i][0])
    escrever(aviso, fonte_pequena, cor_aviso, (LARGURA // 2, 500), True)
    pygame.display.update()
    
def tela_menu():
    botoes = []
    for i in range(len(PROJETOS)):
        botoes.append(pygame.Rect(200, 190 + i * 90, 400, 60))
    aviso = ""
 
    while True:
        relogio.tick(30)
        escolhido = None
 
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(botoes)):
                    if botoes[i].collidepoint(ev.pos):
                        escolhido = i
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return
                elif ev.key == pygame.K_1:
                    escolhido = 0
                elif ev.key == pygame.K_2:
                    escolhido = 1
                elif ev.key == pygame.K_3:
                    escolhido = 2
 
        if escolhido is not None:
            nome, arquivo = PROJETOS[escolhido]
            desenhar_menu(botoes, "Abrindo... (os jogos de texto rodam no terminal)", AZUL)
            ok = abrir_projeto(arquivo)
            pygame.event.clear()
            if ok:
                aviso = ""
            else:
                aviso = "Erro ao abrir o projeto. Confira se todos os arquivos estão na mesma pasta."
 
        desenhar_menu(botoes, aviso, VERMELHO)
        
def main():
    dados = tela_login()
    if dados is not None:
        email, senha = dados
        if tela_senha(senha):
            tela_menu()
    pygame.quit()
 
 
if __name__ == "__main__":
    main()