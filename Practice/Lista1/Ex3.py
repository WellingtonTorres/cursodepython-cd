# 3. Peça ao usuário para digitar uma frase qualquer e: 
# a)  Separe as palavras da frase em uma lista. - OK
# b)  Usando list comprehension, crie uma nova lista contendo apenas as palavras com mais 
# de 4 letras. 
# c) Exiba as duas listas. 
# Exemplo de entrada e saída: 
 
# Entrada: "Python é uma linguagem poderosa e divertida" 
# Lista original: ['Python', 'é', 'uma', 'linguagem', 'poderosa', 'e', 
# 'divertida'] 
# Lista filtrada: ['Python', 'linguagem', 'poderosa', 'divertida'] 

palavras = input("Digite as palavras: ").split()
print(f'Palavras: {palavras}')