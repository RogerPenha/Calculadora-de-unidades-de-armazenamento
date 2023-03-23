from calculadora-de-conversão-de-unidades-de-armazenamento import converterStringParaFloat, BitParaByte, ByteParaBit,ByteParaQuilobyte, QuilobyteParaByte, QuilobyteParaMegabyte, MegabyteParaQuilobyte, MegabyteParaGigabyte, GigabyteParaMegabyte, GigabyteParaTerabyte, TerabyteParaGigabyte, TerabyteParaPetabyte, PetabyteParaTerabyte    

print('BitParaByte \n ByteParaBit')
funcEscolha = input()
if(FuncEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = BitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = ByteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)
