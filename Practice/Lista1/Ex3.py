# 3. Peça ao usuário para digitar uma frase qualquer e: 
# a)  Separe as palavras da frase em uma lista. - OK
# b)  Usando list comprehension, crie uma nova lista contendo apenas as palavras com mais
# de 4 letras. - OK
# c) Exiba as duas listas. - OK
# Exemplo de entrada e saída: 
 
# Entrada: "Python é uma linguagem poderosa e divertida" 
# Lista original: ['Python', 'é', 'uma', 'linguagem', 'poderosa', 'e', 
# 'divertida'] 
# Lista filtrada: ['Python', 'linguagem', 'poderosa', 'divertida'] 

frase = input("Digite as palavras: ").split()
maior4Letras = []
print(f'Palavras: {frase}')
maior4Letras = [palavra for palavra in frase if len(palavra) > 3 ]
print(f'Lista apenas com mais de 4 letras: {maior4Letras}')
