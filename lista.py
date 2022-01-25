# declaração de uma lista (nas outras linguagens chama-se ARRAY - Vetor)
nomes = ['juan', 'kauanny', 'jorge', 'diogo', 'rAfael']
idades = [46,18,38,30,43,38]
print(nomes)
print(idades)

#listar um unico elemento da lista
print(nomes[2].title())
print(nomes[0].title())

#concatenar valores de listas
mensagem = "O aluno da posição 3 é o "+nomes[3].title()+" e a sua idade é:" ,idades[3]
print(mensagem)

#alterar valor da lista
motos = ['honda','yamaha','kwasaki']
print(motos)
motos[0] = 'ducati'
print(motos)

# acrescentar valores ao final da  lista - append(conteúdo)
motos.append('honda')
print(motos)
print(motos[3])

# inserir novos elementos na lista em posição determinada
print("inserir novos elementos")
frutas = ['banana','maçã','laranja']
frutas.insert(1,'pêra')
print(frutas)

#apagar um elemento da lista
del frutas[1]
print(frutas)

# ordenação - sort() modifica as posições dos elementos dentro da lista
#print(nomes)
#nomes.sort()
#print(nomes)

# ordenar a lista sem alterar a listagem original
print('lista original')
print(nomes)
print('lista ordenada temporariamente')
print(sorted(nomes))
print(nomes)

# ordem reversa
print('Ordem inversa de apresentação')
nomes.reverse()
print(nomes)

#tamanha da lista  lenght (tamanho)
print("tamanho da lista: ",len(nomes))

# criando listas numéricas
# range()



