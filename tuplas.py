# tuplas são criadas e não podem ser modificadas em tempo de exedcução
# tupla
dimensoes = (200, 50, 30, 58, 70)
print(dimensoes[0])
print(dimensoes[1])
#dimensoes[0] = 400
#print(dimensoes[0])

print("----------------")
print("Percorrendo elementos da tupla")

for d in dimensoes:
    print(d)

print("conteúdo t1 que é uma tupla")
t1 =(1,)
print(t1[0])

lista = list(t1)
print(lista[0],type(lista))
lista[0] = 2
print(lista[0])

tupla = tuple(lista)
print(tupla[0])
tupl
print(tupla[0])
# lista[0] = 4a
