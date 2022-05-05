# Definindo o número de alunos que precisam estar presentes
print("Digite o número de alunos presentes na aula:")
numeroDeAlunos = input()
# Checando se não foi digitado algo diferente de um número ou digitado 0
if not (numeroDeAlunos.isdigit())  or int(numeroDeAlunos) == 0:
    print("Digite somente número inteiro positivo acima de 0.")
    exit()
#Capturando os horários de chegada
print("Digite o tempo de chegada dos alunos: (Separados por vírgula) )" )
tempoChegada = input()
#separa os horários informados para criar um array com os tempos de chegada
horarios = tempoChegada.split(',')
#requisitoAula corresponde a variável que contará os alunos pontuais na sala (aqueles que o horário for menor ou igual a zero).
requisitoAula = 0
#checando os horários de chegada
for emTempo in horarios:
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