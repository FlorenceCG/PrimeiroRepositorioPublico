def conversor_decimal_binario(decimal):
    binario = ''
    while decimal > 0:
        binario += str(decimal % 2)
        decimal //= 2
    return binario[::-1]


n_decimal = (input("Digite um número: "))
if n_decimal.isnumeric():
    n_decimal = int(n_decimal)

    print('Número na base binária: ', n_decimal)
    print(("Conversão para a base binária: " + conversor_decimal_binario(n_decimal)))

else:
    exit('Entre com um valor numérico inteiro. ')
