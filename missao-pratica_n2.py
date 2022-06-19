def conversor_decimal_binario(decimal):
    binario = ''
    while decimal > 0:
        binario += str(decimal % 2)
        decimal //= 2
    return binario[::-1]


try:
    n_decimal = eval(input("Digite um número: "))
    print('Número na base binária: ', n_decimal)
    print(("Conversão para a base binária: " + conversor_decimal_binario(n_decimal)))

except:
    print('Entre com um valor numérico. ')