# Análise de caracteres

print('==== DESAFIO 05 ====')

termo = input('Vamos analisar o tipo do caractere que será digitado por você! Escreva algo:')

print('Todos os caracteres digitados são números ou letras?\n', termo.isalnum())

print('Qual o tipo do termo "{}" que foi digitado pelo usuário?\n'.format(termo), type(termo))

print('"{}" é do tipo numérico?\n'.format(termo), termo.isnumeric())

print('"{}" tem somente caracteres numéricos?\n'.format(termo), termo.isdigit())

print('"{}" é um número decimal?\n'.format(termo), termo.isdecimal())

print('"{}" está escrito em minúsculo?\n'.format(termo), termo.islower())

print('"{}" tem as letras iniciais estão em maiúsculo?\n'.format(termo), termo.istitle())
