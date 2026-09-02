from turtle import *
import random

t = Turtle()

def desenhar_plano_cartesiano():
    t.pu()
    t.goto(-400, 0)
    t.pd()
    t.goto(400, 0)
    t.stamp()

    t.pu()
    t.goto(0, -400)
    t.pd()
    t.goto(0, 400)
    t.lt(90)
    t.stamp()
    t.rt(90)

    #Retornando ao centro do plano
    t.pu()
    t.goto(0, 0)
    t.pd()


def desenhar_estrela(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.color(cor)
    for cont in range(5):
        t.fd(tamanho)
        t.rt(144)


def desenhar_hexagono(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.color(cor)
    for cont in range(6):
        t.fd(tamanho)
        t.rt(60)


def desenhar_triangulo(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.color(cor)
    for cont in range(3):
        t.fd(tamanho)
        t.rt(120)


def desenhar_pentagono(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.color(cor)
    for cont in range(5):
        t.fd(tamanho)
        t.rt(72)


def desenhar_circulo(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y - tamanho)
    t.seth(0)
    t.pd()
    t.color(cor)
    t.circle(tamanho)


def desenhar_espiral(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.color(cor)
    for cont in range(24):
        t.fd(cont * (tamanho / 100))
        t.rt(15)


#Desenhando o plano cartesiano
desenhar_plano_cartesiano()

#Quadrante 1 (superior direito): estrela e circulo, em posicoes aleatorias
x = random.randint(22, 278)
y = random.randint(82, 338)
desenhar_estrela(x, y, 100, "black")

x = random.randint(72, 328)
y = random.randint(72, 328)
desenhar_circulo(x, y, 50, "blue")

#Quadrante 2 (superior esquerdo): hexagono em posicao aleatoria
x = random.randint(-338, -142)
y = random.randint(162, 378)
desenhar_hexagono(x, y, 80, "green")

#Quadrante 3 (inferior esquerdo): triangulo em posicao aleatoria
x = random.randint(-378, -122)
y = random.randint(-291, -22)
desenhar_triangulo(x, y, 100, "red")

#Quadrante 4 (inferior direito): pentagono e espiral, em posicoes aleatorias
x = random.randint(47, 273)
y = random.randint(-254, -22)
desenhar_pentagono(x, y, 80, "purple")

x = random.randint(147, 365)
y = random.randint(-309, -159)
desenhar_espiral(x, y, 150, "orange")

mainloop()