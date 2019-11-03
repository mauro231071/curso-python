a = int (input('Entre o primeiro valor: '))
b = int(input('Entre o sengundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}. \nsubtracao: {subtracao}.' 
      '\nMultiplicacao: {multiplicacao}'
      '\nDivisao: {divisao}'''
      '\nResto: {resto}'.format(soma=soma,
                               subtracao=subtracao,
                                resto=resto,
                                multiplicacao=multiplicacao,
                                divisao=divisao))
print(resultado)

# x ='1'
# soma2 = int(x) + 1
# print(soma2)
