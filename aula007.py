color = {'verde':'\033[32m','azul':'\033[34m','ori':'\033[m','yellow':'\033[33m','red':'\033[1;31m'}
print(f'{color["red"]}\nnetflix 2{color["ori"]}')
match (nm:=input('qual é seu nome? ')):
    case _ if nm.isalpha():
        match (idd:=int(input('Qual é a sua idade? '))):
            case _ if idd <= 12:
                print(f'\n{color["yellow"]}{nm}{color["ori"]} Seja bem vindo! Aqui esta alguns filmes recomendados')
                print(f'{color["verde"]}A Pequena Sereia\nPinóquio\nElementos\nTurma da Mônica: Laços\nPatrulha Canina: O Filme\nO Rei Leão\nFrankenweenie\nDivertida Mente e Hotel Transilvânia: Transformonstrão{color["ori"]}')
            case _ if 12<idd<18:
                print(f'\n{color["yellow"]}{nm}{color["ori"]} Seja bem vindo! Aqui esta alguns filmes e jogos recomendados')
                print(f'\nFilmens:{color["azul"]}E. T. O Extraterrestre (1982)\nQuerida Encolhi as Crianças (1989)\nO Menino Maluquinho (1995)\nShrek (2001)\nHarry Potter e a Pedra Filosofal (2001)\nMadagascar (2005)\nMeu Malvado Favorito (2010)\nFrankenweenie (2012)\n{color["ori"]}Jogos:{color["azul"]}Fortnite.\nLeague of Legends\nCrossFire\nRoblox\nPUBG.Minecraft\nLost Ark\nCounter-Strike: Global Offensive.{color["ori"]}\n')
            case _ if idd>=18:
                print(f'\n{color["yellow"]}{nm}{color["ori"]} Seja bem vindo! Aqui esta alguns filmes e jogos recomendados')
                print(f'\nFilmens:')
    case _:
        print(f'O nome {'\033[31m'}{nm}{color["ori"]} não pode ser reconhecido')