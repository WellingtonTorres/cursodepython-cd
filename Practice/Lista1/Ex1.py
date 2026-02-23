# 1. Escreva um programa em Python que: 
# a)  Leia do usuário uma sequência de números inteiros separados por espaço e 
# armazene-os em uma lista. - OK
# b)  Realize as seguintes operações: 
# i. Exiba a lista original. - OK
# ii. Crie uma nova lista apenas com os números pares, mantendo a ordem original. - OK
# iii. Crie outra lista com os elementos da lista original sem o primeiro e o último 
# elemento (use fatiamento). - OK
# iv. Calcule a média dos valores da lista original e exiba. - OK
# v. Encontre o segundo maior valor da lista original. - OK

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
print(f'Média valores Lista original: {mediaLista}')
print(f'Maior valor: {maiorValor}')
print(f'Segundo maior valor: {segMaiorValor}')
