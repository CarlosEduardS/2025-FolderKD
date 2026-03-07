pop = 80000
pop2 = 200000
while True:
    pop += pop * 0.03
    if pop >= pop2:
        print('\nChegou ao seu destino\n')
        break
    print('\nErro ',pop)
