entrada = input('Digite um número: ')

try:
    num = float(entrada.replace(',', '.'))  
    
    if num.is_integer():
        if num % 2 == 0:
            print('Esse número é par!')
        else:
            print('Ele é ímpar!')
    else:
        print('O número não é inteiro, portanto, não pode ser classificado como par ou ímpar.')

except ValueError:
    print('Entrada inválida. Certifique-se de digitar um número válido.')