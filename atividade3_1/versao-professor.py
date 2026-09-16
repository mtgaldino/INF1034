from turtle import *
from random import randint

# Definição
def f(x):
    return x + 2

# Chamada da função + print
print(f(2))

def desenha_quadrado(x, y, lado, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for cont in range(4):
        t.fd(lado)
        t.lt(90)
    t.end_fill()

t = Turtle()
# t.shape("turtle")

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

## Versão sem repetição
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)

t.pu()
t.goto(0, 0)
t.pd()

## Versão com repetição
for cont in range(4):
    # print(cont)
    t.fd(100)
    t.lt(90)

# aqui é onde o quadrado estava sendo desenhado

x = randint(10, 300)
y = randint(10, 300)
desenha_quadrado(x, y, 100, "purple")

t.pu()
t.goto(-200, 200)
t.pd()

t.color("black")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica:")
t.fillcolor(var_color)
t.begin_fill()
t.circle(100)
t.end_fill()

mainloop()