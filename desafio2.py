####################################
###  DADOS QUE PODEM SER ALTERADOS
### numeroDeAlunos = inteiro; //   Define o número de alunos que precisam estar presentes para ter aula
### tempoChegada = [x,x,x] // inteiro, negativo ou positivo (negativo e zero = pontual | positivo = atrasado)
numeroDeAlunos = 3  # equivale ao X na descrição do desafio
tempoChegada = [-2,-1,0,1,2]  #Determine os horários de chegada dos alunos
###
################################
# Checando se não foi digitado algo diferente de um número ou digitado 0
if not (str(numeroDeAlunos).isdigit())  or int(numeroDeAlunos) == 0:
    print("Informe somente número inteiro positivo acima de 0.")
    exit()

#requisitoAula corresponde a variável que contará os alunos pontuais na sala (aqueles que o horário for menor ou igual a zero).
requisitoAula = 0
#checando os horários de chegada
for emTempo in tempoChegada:
    #usando try para checar se não foi digitado algo fora dos padrões nos horários, é esperado apenas números.
    try:
        if (int(emTempo) <= 0):
            #testando se o tempo é menor ou igual 0, se for adiciona um aluno na contagem de alunos pontuais.
            requisitoAula += 1
    except:
        print("Horário de chegada informado inválido, digite número(s) inteiro(s) separado(s) por vírgula!")
        exit()

#Checando se terá aula nos critérios abaixo :

#Primeiro : O número de alunos pontuais não foi suficiente, então a aula será cancelada.
if (requisitoAula < int(numeroDeAlunos)):
    print("Aula cancelada.")
#Segundo : O número de alunos pontuais foi igual ou superior ao mínimo definido, então teremos aulas.
elif (requisitoAula >= int(numeroDeAlunos)):
    print("Aula normal.")