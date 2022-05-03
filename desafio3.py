from itertools import combinations_with_replacement
####################################
###  DADOS QUE PODEM SER ALTERADOS
### n = inteiro; // valor que deseja encontrar dentro do vetor
### valores = [x,x,x] // conjunto de números para compor a soma para encontrar o valor de N
n = 10
valores = [2,3,4]
###
################################
#definindo qual o menor valor fornecido
menor = min(valores)
#definir quantas vezes o menor número obtido pode ser repedido em virtude do numero n fornecido
vezes = int(n / menor)
#lendo o total de numeros fornecidos na lista (vetor)
total = int(len(valores))
#criando variavel para armazenar as possibilidades de repetição dos números nos vetores
resultado = []
# iniciando loop para armazenar as possíveis distribuições de números do vetor
while vezes > 0:
    comb = combinations_with_replacement(valores, vezes)
    for x in comb:
        if (sum(x) == n):
            #vou armazenar apenas as possibilidades cujo resultado da soma dos itens seja igual ao valor n informado
            resultado.append(x)
    vezes -= 1
#nova variável para armazenar o tamanho dos vetores criados acima com intuito de descobrir os menores para exibição
tamanhos = []
#percorrendo o vetor criado acima
for tem in resultado:
    tamanhos.append(len(tem))
#como tenho um novo vetor com o tamanho dos vetores, vou buscar qual é o menor deles
menorTamanho = min(tamanhos)
#exibindo o valor de n
print(n)
#buscando qual o menor resultado exisitente no vetor
for iguais in resultado:
    if (len(iguais) == menorTamanho):
        print(iguais)
