from CalculadoraDeUnidadesDeMedida import converterStringParaFloat, BitParaByte, ByteParaBit, ByteParaQuilobyte, QuilobyteParaByte, QuilobyteParaMegabyte, MegabyteParaQuilobyte, MegabyteParaGigabyte, GigabyteParaMegabyte, GigabyteParaTerabyte, TerabyteParaGigabyte, TerabyteParaPetabyte, PetabyteParaTerabyte    

#Bit para Byte e Vice-Versa

print('-Escreva 1 para BitParaByte \n -Escreva 2 para ByteParaBit \n -Escreva 3 para ByteParaQuilobyte \n -Escreva 4 para Quilobyte Para Byte \n -Escreva 5 para Quilobyte Para Megabyte \n -Escreva 6 para Megabyte Para Quilobyte \n -Escreva 7 para Megabyte Para Gigabyte \n Escreva 8 para Gigabyte Para Megabyte \n Escreva 8 para Gigabyte Para Terabyte \n -Escreva 9 para Terabyte Para Gigabyte \n -Escreva 10 para Terabyte Para petabyte \n -Escreva 11 para petabyte Para Terabyte')
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = BitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = ByteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

#Byte para Quilobyte e vice-versa


elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = ByteParaQuilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = QuilobyteParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

#Quilobyte para Megabyte e Vice-Versa


