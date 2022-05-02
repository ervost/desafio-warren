
# Definindo o número inicial
numero_primario = 1
numero_inicio = numero_primario

adicionado =0

    # Fazendo a reversão do número
while (numero_primario < 1000):
        numero_reverso = 0
        while (numero_primario > 0):  
            remainder = numero_primario % 10  
            numero_reverso = (numero_reverso * 10) + remainder  
            numero_primario = numero_primario // 10  
        #print('Primeiro ' , numero_inicio, ' Segundo ' ,  numero_reverso)
        somando = numero_reverso + numero_inicio
        if (somando < 10000):
            for a in str(somando):
                if (int(a)%2 ==0):
                    passou = False
                    break
                else:
                    passou = True
            if passou:
                print("Número n : ", numero_inicio)
        numero_inicio += 1
        if (numero_inicio % 10 == 0):numero_inicio += 1
        numero_primario = numero_inicio
