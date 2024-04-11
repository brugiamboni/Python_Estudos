# Script criado para calcular o dobro, o triplo e a raíz quadrada de um número digitado pelo usuário.

e = '='*8
print(e, 'DESAFIO 07', e)

n = int(input('Digite um número para descobrir algumas informações sobre ele!'))

d = n * 2
t = n * 3
r = n ** (1/2)

print('Você escolheu o número {}! \n O dobro dele é: {}. \n O triplo dele é: {}. \n A raiz quadrada dele é {:.2f}.'.format(n, d, t, r))
