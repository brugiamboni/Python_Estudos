print('==== DESAFIO 04 ====')

print('CALCULADORA DE SOMAS COM TIPO')

n1 = int(input('Escolha o primeiro número a ser somado:'))
n2 = int(input('Escolha o primeiro número a ser somado:'))

s = n1 + n2

print('O valor resultante da soma entre {} e {} é: {}'.format(n1, n2, s))

print('O tipo do número {} é: '.format(n1), type(n1))
print('O tipo do número {} é: '.format(n2), type(n2))
print('O tipo do número {} resultante da soma entre {} e {} é: '.format(s, n1, n2), type(s))

