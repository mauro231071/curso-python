a = int(input('Digite um valor: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div = x + 1

if div == 2:
    print('Numero {} é primo'. format(a))
else:
     print('numero {} não é primo'. format(a))