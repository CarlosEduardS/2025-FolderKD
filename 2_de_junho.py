import time

while True:
    a = input('\nDe um numero de 1 a 15:\n--= ')
    
    if a.isdigit():
        a = float(a)

        i = 1
        while i <= a < 16:
            if a == 1:
                print(f'{i} numero contado')
            else:
                print(f'\r{i} numeros contados',end='')
            time.sleep(1)
            i += 1
    print('Valor invalido!')