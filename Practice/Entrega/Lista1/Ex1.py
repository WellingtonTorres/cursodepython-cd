# 1. Escreva um programa em Python que: 
# a)  Leia do usuário uma sequência de números inteiros separados por espaço e 
# armazene-os em uma lista. 
# b)  Realize as seguintes operações: 
# i. Exiba a lista original. 
# ii. Crie uma nova lista apenas com os números pares, mantendo a ordem original. 
# iii. Crie outra lista com os elementos da lista original sem o primeiro e o último 
# elemento (use fatiamento). 
# iv. Calcule a média dos valores da lista original e exiba. 
# v. Encontre o segundo maior valor da lista original. 
# c) Mostre todas as listas e os resultados calculados. 
# Exemplo de entrada e saída: 
# Digite os números: 10 3 8 15 22 7 
# Lista original: [10, 3, 8, 15, 22, 7] 
# Lista de pares: [10, 8, 22] 
# Lista sem o primeiro e último: [3, 8, 15, 22] 
# Média: 10.83 
# Segundo maior valor: 15
#Exercicio 1
sequencia = input("Digite uma sequência de números inteiros separados por espaço: ")
dadosLista = []
listaPares = []
listaFatiada = []
mediaLista = 0
maiorValor = 0
segMaiorValor = 0
dadosTratados = []

for atual in sequencia.split():
    numero = int(atual)
    dadosLista.append(numero)
    if numero % 2 == 0:
        listaPares.append(numero)
        
listaFatiada = dadosLista[1:len(dadosLista)-1]
mediaLista = sum(dadosLista) / len(dadosLista)

# Segundo maior valor
dadosTratados = list(set(dadosLista)) #remove duplucados
#print(f'Dados tratados: {dadosTratados}')
maiorValor = max(dadosTratados)
dadosTratados.remove(maiorValor)
segMaiorValor = max(dadosTratados)
        
print(f'Lista original: {dadosLista}')
print(f'Lista de pares: {listaPares}')
print(f'Lista fatiada: {listaFatiada}')
print(f'Média valores Lista original: {mediaLista:.2f}')
print(f'Maior valor: {maiorValor}')
print(f'Segundo maior valor: {segMaiorValor}')
