s = '='*8

print(s, 'DESAFIO 6', s)

n = int(input('Escolha um número do qual você quer saber qual é seu antecessor e seu sucessor:'))
a = n -1
s = n +1

print('O antecessor de {} é: {} \nO sucessor de {} é: {}'. format(n, a, n, s))

# Observações do programa #

# int é para deixar uma string como número inteiro #
# /n é para quebrar linhas #
# end= ' ' é usado quando não quero ter quebra de linha quando uso mais de um 'print' #
