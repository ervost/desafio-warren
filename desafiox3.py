from itertools import combinations_with_replacement
### n = inteiro; // valor que deseja fazer as somas para encontrar o menor vetor
### valores = [x,x,x] // conjunto de números para compor a soma para encontrar o valor de N
print("Digite o número N (valor cuja soma deve ser encontrada:")
n = input()
# checando se o valor digitado é válido
if not (n.isdigit())  or int(n) == 0:
    print("Digite somente número inteiro positivo acima de 0.")
    exit()
else:
    n = int(n)
    
print("Digite a matriz cuja soma deve ser feita para encontrar N: (Separados por vírgula) )" )
try:
    valores = eval(input())
except:
    print("Digite apenas números separados por vírgula!")
    exit()

#definindo qual o menor valor fornecido
menor = int(min(valores))
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
#preciso checar se os valores digitados deram algum resultado.
if not tamanhos:
    print("Nenhum valor encontrado!")
    exit()

#como tenho um novo vetor com o tamanho dos vetores, vou buscar qual é o menor deles
menorTamanho = min(tamanhos)
#exibindo o valor de n

#buscando qual o menor resultado exisitente no vetor
for iguais in resultado:
    if (len(iguais) == menorTamanho):
        print(iguais)