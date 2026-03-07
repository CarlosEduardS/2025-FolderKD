import datetime

total = 0.0
estoque = []

while True:
    nome = input('Digite o nome do produto\n').title()
    pre = float(input('Digite o preço do produto\n'))
    
    dic = {'Nome': '',
           'Preço': 0,}
    
    dic['Nome'] = nome
    dic['Preço'] = pre
    estoque.append(dic)
    total += pre
    
    if (res:=input('Deseja adicionar mais um item? [s/n]\n').lower()) == 's':
        continue
    elif res == 'n':
        break
    else:
        print('Erro... Digite novamente.\n')

print("\n--- Estoque Final ---\n")
for i in estoque:
    print(f"Nome: {i['Nome']}, Preço: R$ {i['Preço']:.2f}")
print(f'\nTotal: R$ {total:.2f}')
print(f'\nRegistro feito as: {datetime.datetime.today()}')