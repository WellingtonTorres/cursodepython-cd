# 2. Peça ao usuário para digitar uma lista de números inteiros separados por espaço e: 
# a)  Converta-os para uma lista de inteiros. - OK
# b)  Crie, usando list comprehension, uma nova lista contendo o quadrado de cada número
# da lista original. - OK
# c) Exiba as duas listas. - OK
# Exemplo de entrada e saída: 
# Entrada: 2 3 4 
# Saída: [4, 9, 16]

# Usar map ao inves de for

# lista = input("Digite uma sequência de números inteiros separados por espaço: ").split()
# print(f'Lista original: {lista}')
# listaConvertida = list(map(int, lista))
# print(f'Lista Convertida: {listaConvertida}')
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

listNumbers = list(map(int, input("Digite uma sequência de números inteiros separados por espaço: ").split()))
print(f'Lista Convertida: {listNumbers}')
listSquare = [itemNumber ** 2 for itemNumber in listNumbers]
print(f'Lista Quadrada: {listSquare}')