#pip install langdetect googletrans==4.0.0-rc1

import langdetect as ld
from googletrans import Translator

def lotom(texto,des):
    tradutor = Translator()
    traduçao = tradutor.translate(texto, src=ld.detect(texto),dest=des)
    return traduçao.text
while True:
    tra = lotom(input('Digite algo: '),input('(escreva a sigla da lingua)Para qual lingua deseja traduzir? '))
    print(f'O testo traduzido fica: {tra}')