# 4. Peça ao usuário para digitar um texto qualquer e: 
# a)  Separe todas as palavras do texto em uma lista (considere que as palavras são separadas 
# por espaço). 
# b)  Converta essa lista em um set, para obter apenas as palavras únicas (eliminando 
# repetições). 
# c) Exiba: 
# • A quantidade de palavras diferentes no texto. 
# • A lista das palavras únicas em ordem alfabética.

palavras = input("Digite as palavras: ").split()
# Notei que ao usar set ele elimina duplicado,
# porém não mantém a ordem
# palavrasUnicas = list(set(palavras))

palavrasUnicas = list(dict.fromkeys(palavras))
palavrasOdenadas = sorted(palavrasUnicas)

print(f'Entrada: {palavras}')
print(f'Palavras únicas: {palavrasUnicas}')
print(f'Quantidade: {len(palavrasUnicas)}')
print(f'Em ordem: {palavrasOdenadas}')
