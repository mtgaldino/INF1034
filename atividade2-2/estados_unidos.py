from turtle import *

t = Turtle()

largura = 500
altura_total = 350
altura_faixa = altura_total / 13

y = 175
for cont in range(13):
    t.pu()
    t.goto(-largura / 2, y)
    t.pd()
    t.seth(0)
    if cont % 2 == 0:
        t.color("#B22234")
    else:
        t.color("white")
    t.begin_fill()
    for lado in range(2):
        t.fd(largura)
        t.rt(90)
        t.fd(altura_faixa)
        t.rt(90)
    t.end_fill()
    y -= altura_faixa

#Desenhando o cantao azul
largura_canto = largura * 0.4
altura_canto = altura_total * (7 / 13)
t.pu()
t.goto(-largura / 2, 175)
t.pd()
t.seth(0)
t.color("#3C3B6E")
t.begin_fill()
for lado in range(2):
    t.fd(largura_canto)
    t.rt(90)
    t.fd(altura_canto)
    t.rt(90)
t.end_fill()

#Desenhando a grade de estrelas dentro do cantao
linhas = 4
colunas = 5
espaco_x = largura_canto / (colunas + 1)
espaco_y = altura_canto / (linhas + 1)

for lin in range(1, linhas + 1):
    for col in range(1, colunas + 1):
        cx = -largura / 2 + col * espaco_x
        cy = 175 - lin * espaco_y
        t.pu()
        t.goto(cx, cy)
        t.pd()
        t.seth(0)
        t.color("white")
        t.begin_fill()
        for ponta in range(5):
            t.fd(10)
            t.rt(144)
        t.end_fill()

mainloop()
