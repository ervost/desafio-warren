#criando função para reverter o número
def reverter(numero):
    numero_reverso = 0
    while (numero > 0):  
        remainder = numero % 10  
        numero_reverso = (numero_reverso * 10) + remainder  
        numero = numero // 10  
    #retornando o número invertido
    return numero_reverso

# Definindo o número inicial (objetivo proposto é de 1 até 1000)
numero_inicio = 1

# Fazendo os cálculos entre as possibilidades
while (numero_inicio < 1000):
        somando = reverter(numero_inicio) + numero_inicio
        #o limite da soma deve ser 1 milhão
        if (somando < 1000000):
            for a in str(somando):
                #testando se na soma o número é par ou impar, se for par já para o loop e prossegue para o próximo
                if (int(a)%2 ==0):
                    passou = False
                    break
                else:
                    passou = True
            if passou:
                print("Número n : ", numero_inicio)
        #incrementando para o próximo número
        numero_inicio += 1
        #simples condicional para retirar os números com final 0, como 100,200,... critério imposto pelo desafio (sem iniciar com 0)
        if (numero_inicio % 10 == 0):numero_inicio += 1
