
def para_binario(texto):
  binario = ""
  for caractere in texto:
    if caractere.isalpha()  or caractere == " ":
      valor_ascii = ord(caractere)
      binario += bin(valor_ascii)[2:].zfill(8) + " "
  if caractere.isdigit():
    valor_numerico = int(texto)
    binario += bin(valor_numerico)[2:].zfill(8) + " "
  return binario.strip()
while True:
    texto = input('Escreva algo: ')
    binario = para_binario(texto)
    print(f"O texto '{texto}' em binário é: {binario}")
