from turtle import *

t = Turtle()
# t.shape("turtle")

#Desenhando o plano cartesiano
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

#retornando ao centro do plano
t.pu()
t.goto(0, 0)
t.pd()

## Versão com repetição
# for cont in range(4):
#     # print(cont)
#     t.fd(100)
#     t.lt(90)



t.pu()
t.goto(200, 200)
t.pd()

#Desenhando a estrela
for cont in range(5):
	t.fd(100)
	t.rt(144)

#Desenhando o quadrado
# t.color("yellow")
# t.fillcolor("purple")
# t.begin_fill()
# for cont in range(4):
#     t.fd(100)
#     t.lt(90)
# t.end_fill()

t.pu()
t.goto(-200, 200)
t.pd()

#Desenhando o hexagono
for cont in range(6):
	t.fd(80)
	t.rt(60)

#Desenhando o triangulo
t.pu()
t.goto(-200, -200)
t.pd()
for cont in range(3):
	t.fd(100)
	t.rt(120)

#Desenhando o pentagono
t.pu()
t.goto(200, -200)
t.pd()

for cont in range(5):
    t.fd(80)
    t.rt(72)

#Desenhando uma espiral (desafio extra) 
t.pu()
t.goto(200, -200)
t.pd()
for cont in range(40):
	t.fd(cont * 2)
	t.rt(15)

mainloop()