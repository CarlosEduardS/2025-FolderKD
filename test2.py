def atleta(nm,idd,exps,gene):
    if nm.isalpha():
        if idd <= exps:
            if gene.isalpha():
                print(f'{nm} Você é {idd}, sua experiencia é de {exps}, e você participara da competição {gene}')
            else:
                print('\033[31mErro 404\033[m')
        else:
            print('\033[31mErro 404\033[m')
    else:
        print('\033[31mErro 404\033[m')
    pass
def idade(idade):
    idh = idade
    match idh:
        case _ if idh <= 8:
            idd = "Muito jovem para competir"
        case _ if 8<idh<=12:
            idd = "Categoria Infantil"
        case _ if 13<=idh<=17:
            idd = "Categoria Juvenil"
        case _ if idh >= 18:
            idd = "Categoria Sênior"
        case _:
            idd = 'Erro 404'
    return idd
def exp(experiencia):
    exper = experiencia
    match exper:
        case _ if 0<exper < 1:
            exps = 'Iniciante'
        case _ if 1<=exper<=3:
            exps = 'Intermediario'
        case _ if exper > 3:
            exps = 'Avançado'
        case _ if exper:
            exps = 'um cabaço sem experiencia'
    return exps
def gen(genero):
    match genero:
        case _ if genero[0:2] == 'mas' or genero[0] == 'm' or genero[0:1] == 'ma':
            gene = 'Masculina'
        case _ if genero[0:2] == 'fes' or genero[0] == 'f' or genero[0:1] == 'fe':
            gene = 'Feminina'
        case _:
            gene = 'Error 404'
    return gene

exps = exp(float(input('Qual é sua experiencia? ')))
idd = idade(float(input('Qual é a sua idade? ')))
print('-'*90,'\nEscreva seu genero como m p/ masculino e f p/ feminino\n','-'*90)
gene = gen(input('Qual é seu genero? ').lower())
pri = atleta(input('Qual é seu nome: '),idd,exps,gene)
